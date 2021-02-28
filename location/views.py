from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from location.models import Location, Restaurant


class LocationModelViewSet:
    # add permission class to create
    pass