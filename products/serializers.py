from rest_framework import serializers
from products.models import Category, Product
from location.serializers import StoreModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    sold_by = StoreModelSerializer(
        read_only=True,
        fields=["id", "name", "address", "code", "in_school"],
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "base_charge",
            "addition_charge",
            "measured_in",
            "category",
            "available",
            "countable",
            "sold_by",
        ]
