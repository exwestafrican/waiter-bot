from users.selectors import get_user
from commands.selectors import (
    is_valid_command,
    get_command_list,
    get_example,
    get_a_random_command,
)
from messaging.utils import find_command_in_message


def get_name_or_number(number):
    user = get_user(phone_number=number)
    if user:
        return user.first_name
    else:
        return number


def valid_command_in_message(msg, sender):
    command = find_command_in_message(msg, sender)
    if command.get("found"):
        if is_valid_command(command.get("data")):
            return {
                "success": True,
                "message": "",
                "data": {"command": command.get("data")},
            }
        else:
            commands = ", ".join(get_command_list()[:5])
            random_command = get_a_random_command()
            example = get_example(random_command)
            return {
                "success": False,
                "message": "hey {}, {} is not a valid command, here are a list of valid commands you could use: {} to use one, simply do {}".format(
                    sender, command.get("data"), commands, example
                ),
                "data": {"command": ""},
            }

    elif command.get("found") is False:
        return {
            "success": False,
            "message": command.get("message"),
            "data": {"command": ""},
        }
