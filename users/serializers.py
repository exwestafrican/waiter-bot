from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_auth.registration.serializers import RegisterSerializer
import re

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
        regex = r"^\+234\d{10}$"
        match = re.match(regex, phone_number)
        phone_number_exits = User.objects.filter
        if not match:
            raise serializers.ValidationError(
                "{} is not a valid phone number please try something like +234090334..".format(
                    phone_number
                )
            )
        elif phone_number_exits(phone_number=phone_number).exists():
            raise serializers.ValidationError(
                "{} exists please try a different one or contact us to retrieve your account".format(
                    phone_number
                )
            )

        else:
            return phone_number

    def custom_signup(self, request, user):
        customer_group = Group.objects.get(name="customer")
        customer_group.user_set.add(user)
        user.phone_number = self.validated_data.get("phone_number")
        user.save()
