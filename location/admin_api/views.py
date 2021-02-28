# rest imports
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from location.models import Location

from utils.mixins import ModelMixins


class RestaurantAdminModelViewSet(ModelMixins):
    model = Location
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        self.model.objects.all()
