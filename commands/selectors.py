command_list = ["order"]

from commands.models import Command


def get_command_list():
    return list(Command.objects.all().values_list("name", flat=True))


def get_command(name):
    return Command.objects.get(name=name)


def get_example(command):
    try:
        return command.example
    except AttributeError:
        command = get_command(command)
        return command.example


def is_valid_command(command):
    return Command.objects.filter(name=command).exists()


def get_a_random_command():
    return Command.objects.first()