from rest_framework import serializers
from cart.models import Cart, CartItem
from products.selectors import product_exists
from users.selectors import get_user
from cart.services import create_cart

from payment_gateway.processor import payment_processor
from messaging.twillio_msg import send_text_message
from utils.helper_func import convert_to_kobo


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ["product", "product_name", "quantity", "total"]
        read_only_fields = ["id"]

    def get_product_name(self, obj):
        return obj.product.name


class CartSerializer(serializers.ModelSerializer):
    cart_item = CartItemSerializer(many=True)
    status = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = [
            "id",
            "owner",
            "contact",
            "name",
            "email",
            "bought_by",
            "delivery_address",
            "status",
            "cart_item",
            "fees",
            "items_total",
            "reference",
        ]
        read_only_fields = ["id", "owner"]
        extra_kwargs = {"contact": {"required": True}}

    def get_status(self, obj):
        return obj.status.name

    def validate(self, data):
        cart_item = data.get("cart_item")
        for product in cart_item:
            if not product_exists(id=product.get("product").id):
                raise serializers.ValidationError(
                    "{} does not exist".format(product.get("product"))
                )
            return data

    def create(self, validated_data):
        cart_item = validated_data.pop("cart_item")
        owner = get_user(phone_number=validated_data.get("contact"))
        cart = create_cart(owner=owner, **validated_data)
        for product in cart_item:
            CartItem.objects.create(cart=cart, **product)
        self.inform_customer(cart)
        return cart

    def inform_customer(self, cart):
        amount = convert_to_kobo(cart.items_total + cart.fees)
        payload = {
            "email": cart.email,
            "amount": amount,
            "currency": "NGN",
            "channels": ["card", "bank"],
            "reference": str(cart.id),
        }
        trans = payment_processor.initialize_transaction(payload)
        if trans["status"] is True:
            payment_link = trans["data"]["authorization_url"]
            msg = "hey your order is pending, checkout the summary on https://mobilewaiter.netlify.app/store/checkout/{}  pay with this {} so we can start processing your order.".format(
                cart.id, payment_link
            )

            send_text_message(cart.contact, msg)

    def update(self, instance, validated_data):
        instance.contact = validated_data.get("contact", instance.contact)
        instance.delivery_address = validated_data.get(
            "delivery_address", instance.delivery_address
        )
        instance.bought_by = validated_data.get("bought_by", instance.bought_by)
        instance.status = validated_data.get("status", instance.status)
        new_items = validated_data.get("cart_item")
        instance.cart_item.all().delete()
        for product in new_items:
            CartItem.objects.create(cart=instance, **product)

        return instance
