from rest_framework import serializers
from products.models import Product


class ProductModelSerializer(models.Model):
    class Meta:
        model = Product
        fields = ["name", "sold_by", "countable", "is_available", "measured_in"]