from users.selectors import get_user
from commands.selectors import is_valid_command, get_command_list
from commands.utils import find_command_in_message


def get_name_or_number(number):
    user = get_user(phone_number=number)
    if user:
        return user.first_name
    else:
        return number


def valid_command_in_message(msg):
    command = find_command_in_message(msg)

    if command.get("found"):
        command = is_valid_command(command)
        return {"success": True, "message": "", "data": {"command": command}}
        
    elif command.get("found") is False:
        return {
            "success": False,
            "message": command.get("message"),
            "data": {"command": ""},
        }
    else:
        commands = ", ".join(get_command_list()[10])
        example = get_example(commands[0])
        return {
            "success": False,
            "message": "You didn't use a valid command, here are a list of valid command: {commands} to use one, simply do {}".format(
                commands, example
            ),
            "data": {"command": ""},
        }
