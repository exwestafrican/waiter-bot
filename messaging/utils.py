import re


def find_command(mgs):
    regex = r"^#\s?\w+"
    match = re.match(regex, msg)
    if not match:
        return "Hey, you didn't give a command please not all commands start with  a '#' e.g #order "
    else:
        command = match.group()
        valid_command = validate_command(command)
        if valid_command:
            pass
        else:
            return "Opps!! {} is not a valid command please #valid_commands to get a list of valide commands".format(
                command
            )


def clean_data(data):
    return data.strip()


command_list = ["order"]


def validate_command(command):
    cmd = command.lower()
    # make data base call
    if cmd in command_list:
        return True
    return False


def handle_command(command):
    # call a service
    pass