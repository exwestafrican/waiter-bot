from rest_framework import serializers
from cart.models import OrderStatus


class OrderStatusAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ["name"]
        extra_kwargs = {"name": {"required": True}}
