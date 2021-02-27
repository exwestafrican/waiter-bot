command_list = ["order"]

from commands.models import Command


def get_command_list():
    return list(Command.objects.all().values_list("name", flat=True))
