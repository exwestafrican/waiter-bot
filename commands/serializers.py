from commands.models import Command
from rest_framework import serializers
import re


class CommandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = [
            "name",
            "description",
            "example",
        ]

    def validate_name(self, name):
        regex = r"^\D\w*[^-+]\S$"
        match = re.match(regex, phone_number)
        if match:
            return name
        raise serializers.ValidationError(
            "{} is not a valid command format, please avoide spaces or special charachets like '@+*".format(
                name
            )
        )
