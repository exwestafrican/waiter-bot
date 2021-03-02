from rest_framework import serializers
from cart.models import Cart, CartItem
from products.selectors import product_exists


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        field = ["id", "product", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    cart_item = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cart
        fields = [
            "id",
            "owner",
            "contact",
            "bought_by",
            "delivery_address",
            "status",
            "cart_item",
        ]
        read_only_fields = ["id"]

    def validate(self, data):
        cart_item = data.get("cart_item")
        for product in cart_item:
            if not product_exists(id=product.get("id")):
                raise serializers.ValidationError(
                    "{} does not exist".format(product.get("product"))
                )
            return data

    def save(self, validated_data):
        cart_item = validated_data.pop("cart_item")
        Cart.objects.create(**validated_data)
        for product in cart_item:
            CartItem.objects.create(**product)
