from rest_framework import serializers
from location.models import Location


class LocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["area", "state", "popular_name"]
