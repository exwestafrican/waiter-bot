from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from location.models import Location
from utils.mixins import ModelMixins
from location.serializers import LocationModelSerializer


class LocationModelViewSet(ModelMixins):
    model = Location
    permission_classes = [IsAuthenticated]
    serializer_class = LocationModelSerializer

    def get_queryset(self):
        return self.model.objects.all()

    def create(self):
        # raise not implimented
        pass