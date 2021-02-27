from commands.models import Command
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import re


class CommandModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=15,
        validators=[
            UniqueValidator(
                queryset=Command.objects.all(),
                message="command with the same name exists",
            )
        ],
    )

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
