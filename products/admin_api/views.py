from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from products.models import Product
from products.admin_api.services import change_status_of_product, create_product
from products.admin_api.serializers import ProductModelAdminSerializer

from utils.mixins import ModelMixins


class ProductAdminModelViewSet(ModelMixins):
    model = Product
    permission_classes = [IsAuthenticated]
    serializer_class = ProductModelAdminSerializer

    def get_queryset(self):
        return self.model.objects.all()

    @action(methods=["put"], detail=True)
    def change_product_status(self, request, pk=None):
        product = self.get_object()
        change_status_of_product(product)
        return Response(
            {"success": True, "message": "successfully changed status", "data": ""}
        )

    def perform_create(self, serializer):
        admin = self.request.user
        create_product(admin, **serializer.validated_data)
