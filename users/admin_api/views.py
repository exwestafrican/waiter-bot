from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from users.admin_api.serializer import RoleChangeSerializer
from users.admin_api.services import change_users_role
from users.serializers import UserDetailModelSerializer

User = get_user_model()


class UserAdminModelViewSet(viewsets.ModelViewSet):
    model = User
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserDetailModelSerializer

    @action(detail=True, methods=["post"])
    def change_users_role(self, request, pk=None):
        admin = request.user
        user = self.get_object()
        serializer = RoleChangeSerializer(data=request.data)
        if serializer.is_valid():
            role_change = change_users_role(admin, user, **serializer.validated_data)
            if role_change:
                return Response(
                    {
                        "success": True,
                        "message": "you've successfully changed {}'s role to {}".format(
                            user.first_name, serializer.validated_data.get("new_role")
                        ),
                        "data": "",
                    },
                    status=status.HTTP_200_Ok,
                )
            return Response(
                {
                    "success": False,
                    "message": "role could not be changed because {} does not exist".format(
                        serializer.validated_data.get("new_role")
                    ),
                    "data": "",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            return Response(
                {
                    "success": False,
                    "message": "you did something wrong",
                    "data": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
