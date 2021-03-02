from rest_framework import serializers
from cart.models import Cart, CartItem



class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            "id",
            "cart",
            "owner",
            "contact",
            "bought_by",
            "delvery_address",
            "status",
        ]
        read_only_fields = ["id"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        field = ["product", "quantity"]
