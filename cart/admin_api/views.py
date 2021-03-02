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

    @action(methods=["post"], detail=False)
    def create_status(self, request):
        admin = request.user
        serializer = OrderStatusAdminSerializer(data=request.data)
        if serializer.is_valid():
            create_order_status(admin, **serializer.validated_data)
            return Response(
                {"success": True, "message": "status created", "data": ""},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"success": False, "message": "failed", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
