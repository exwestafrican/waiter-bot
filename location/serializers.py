from rest_framework import serializers
from location.models import Location, Store
from utils.dynamic_serializers import DynamicFieldsModelSerializer

class LocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["area", "state", "popular_name"]


class StoreModelSerializer(serializers.ModelSerializer):
    available_in = LocationModelSerializer(read_only=True, many=True)

    class Meta:
        model = Store
        fields = ["id", "name", "owner", "address", "available_in", "code", "in_school"]

    
