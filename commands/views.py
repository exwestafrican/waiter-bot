from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from commands.models import Command
from commands.serializers import CommandModelSerializer


class CommandModelViewSet(viewsets.ModelViewSet):
    model = Command
    serializer_class = CommandModelSerializer

    def get_queryset(self):
        return Command.objects.all()
