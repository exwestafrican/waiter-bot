# rest imports
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from location.models import Location, Restaurant
from location.admin_api.serializers import (
    LocationModelAdminSerializer,
    RestaurantModelAdminSerializer,
)
from utils.mixins import ModelMixins


class RestaurantAdminModelViewSet(ModelMixins):
    model = Restaurant
    permission_classes = [IsAuthenticated]
    serializer_class = RestaurantModelAdminSerializer

    def get_queryset(self):
        return self.model.objects.all()


class LocationAdminModelViewSet(ModelMixins):
    model = Location
    permission_classes = [IsAuthenticated]
    serializer_class = LocationModelAdminSerializer

    def get_queryset(self):
        self.model.objects.all()

    def perform_create(self, serializer):
        admin = self.request.user
        serializer.save(admin)
