from django.db import models

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


class TimeStampMixin(models.Model):
    "determins when model was created and edited"
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """
        declearing abstract class allows class attributes to be used as fields
        when inherited
        """

        abstract = True

    def __str__(self):
        return self.name


class ModelMixins(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {"success": True, "message": "successful", "data": serializer.data},
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        else:
            return Response(
                {"success": False, "message": "failed", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {"success": True, "message": "successful", "data": serializer.data},
            status=status.HTTP_200_OK,
        )
