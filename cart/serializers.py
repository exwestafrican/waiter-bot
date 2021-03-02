from rest_framework import serializers
from cart.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        field = ["id", "product", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    cart_item = CartItemSerializer(many=True)

    class Meta:
        model = CartItem
        fields = [
            "id",
            "owner",
            "contact",
            "bought_by",
            "delvery_address",
            "status",
        ]
        read_only_fields = ["id"]


