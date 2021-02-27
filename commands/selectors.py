command_list = ["order"]

from commands.models import Command


def get_command_list():
    return list(Command.objects.all().values_list("name", flat=True))


def get_example(command):
    return command.example_command_format


def is_valid_command(command):
    return Command.objects.filter(name=command).exists()