from rest_framework import serializers
from location.models import Location, Restaurant
from location.admin_api import create_restaurant


class LocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["area", "state", "popular_name"]


class RestaurantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["name", "owner", "address", "available_in", "code", "in_school"]
        extra_kwargs = {"code": {"read_only": True}}

    def save(self):
        create_restaurant(**self.validated_data)
