from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from location.models import Location, Store
from utils.mixins import ModelMixins, ReadOnlyMixins
from location.serializers import LocationModelSerializer, StoreModelSerializer


class LocationModelViewSet(ReadOnlyMixins):
    model = Location
    serializer_class = LocationModelSerializer
    queryset = Location.objects.all()


class StoreModelViewSet(ReadOnlyMixins):
    model = Store
    serializer_class = StoreModelSerializer
    queryset = Store.objects.all()

    @action(methods=["get"], detail=True)
    def view_products(self, request, pk=None):
        vendor = self.get_object()