from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from cart.models import Cart
from cart.serializers import CartSerializer
from utils.mixins import ModelMixins


class CartModelViewSet(ModelMixins):
    model = Cart
    serializer_class = CartSerializer

    def get_queryset(self):
        return self.model.objects.all()
