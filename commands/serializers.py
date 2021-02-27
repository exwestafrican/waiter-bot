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
        # nowhitespace or special character word with(_ as space) nowhitespace or special
        regex = r"^[^#-+@*0_9\s][a-zA-Z_]*[^-+@*#\s]$"
        match = re.match(regex, name)
        if match:
            return name
        raise serializers.ValidationError(
            "{} is not a valid command format, please avoide spaces or special charachets like '@+*".format(
                name
            )
        )
