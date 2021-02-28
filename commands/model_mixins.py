from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


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
