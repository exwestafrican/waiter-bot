from rest_framework import serializers


class RoleChangeSerializer(serializers.Serializer):
    old_role = serializers.CharField(max_length=500, required=False)
    new_role = serializers.CharField(max_length=500)