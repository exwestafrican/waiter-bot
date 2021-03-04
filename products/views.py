from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from products.models import Product
from products.serializers import ProductSerializer
from utils.mixins import ReadOnlyMixins

# Create your views here.
class ProductModelViewSet(ReadOnlyMixins):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer