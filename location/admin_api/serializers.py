from rest_framework import serializers
from location.models import Location, Store
from location.admin_api.services import create_restaurant
from rest_framework.validators import UniqueTogetherValidator


class LocationModelAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["area", "state", "popular_name"]


class StoreModelAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["name", "owner", "address", "available_in", "code", "in_school"]
        read_only_fields = ["code"]
        validators = [
            UniqueTogetherValidator(
                queryset=Restaurant.objects.all(),
                fields=["name", "owner"],
                message="a restaurant with this name and owner already exists",
            )
        ]
