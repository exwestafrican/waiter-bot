from rest_framework import serializers
from products.models import Product
from rest_framework.validators import UniqueTogetherValidator


class ProductModelAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "sold_by",
            "countable",
            "available",
            "measured_in",
            "base_charge",
            "addition_charge",
        ]
        extra_kwargs = {"measured_in": {"required": True}}
        validators = [
            UniqueTogetherValidator(
                queryset=Product.objects.all(),
                fields=["name", "sold_by"],
                message="restaurant already has this product",
            )
        ]
