from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from cart.admin_api.services import create_order_status
from cart.admin_api.serializers import OrderStatusAdminSerializer
from cart.models import OrderStatus
from utils.mixins import ModelMixins


class OrderStatusAdminModelViewSet(ModelMixins):
    model = OrderStatus
    serializer_class = OrderStatusAdminSerializer

    def get_queryset(self):
        return self.model.objects.all()

    def perform_create(self, serializer):
        admin = self.request.user
        create_order_status(admin, **serializer.validated_data)
