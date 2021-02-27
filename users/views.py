# Create your views here.
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

from users.serializers import UserDetailModelSerializer, MyTokenObtainPairSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserDetailModelSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(user=self.request.user)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
