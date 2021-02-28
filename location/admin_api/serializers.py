from rest_framework import serializers
from location.models import Location, Restaurant


class LocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["area", "state", "popular_name"]


class RestaurantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["name", "owner", "address", "available_in", "code", "in_school"]
