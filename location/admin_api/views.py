# rest imports
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from location.models import Location, Store
from location.admin_api.serializers import (
    LocationModelAdminSerializer,
    StoreModelAdminSerializer,
)
from location.admin_api.services import create_store
from utils.mixins import ModelMixins


class StoreAdminModelViewSet(ModelMixins):
    model = Store
    permission_classes = [IsAuthenticated]
    serializer_class = StoreModelAdminSerializer

    def get_queryset(self):
        return self.model.objects.all()

    def perform_create(self, serializer):
        admin = self.request.user
        create_store(admin=admin, **serializer.validated_data)


class LocationAdminModelViewSet(ModelMixins):
    model = Location
    permission_classes = [IsAuthenticated]
    serializer_class = LocationModelAdminSerializer

    def get_queryset(self):
        self.model.objects.all()
