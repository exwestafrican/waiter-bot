from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_auth.registration.serializers import RegisterSerializer
from users.validators import validate_mobile_number

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["username"] = self.user.username
        return data


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


class UserDetailModelSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "date_joined",
            "is_active",
            "phone_number",
            "email",
            "username",
            "groups",
        ]


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=False, write_only=True)
    phone_number = serializers.CharField(required=True)

    def get_cleaned_data(self):
        return {
            "username": "",
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
        }

    def validate_phone_number(self, phone_number):
        return validate_mobile_number(phone_number)

    def custom_signup(self, request, user):
        # call waiter interface
        customer_group = Group.objects.get(name="customer")
        customer_group.user_set.add(user)
        print(request.get("phone_number"))
        user.phone_number = request.get("phone_number")
