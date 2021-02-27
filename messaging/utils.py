import re
from commands.selectors import get_command_list


def find_command_in_message(msg, sender):
    regex = r"^#\s?\w+"
    match = re.match(regex, msg)
    if not match:
        commands = ", ".join(get_command_list()[10])
        example = get_example(commands[0])
        return {
            "found": False,
            "message": "Hey, {} No command found in message we couldn't find any command in your message, here are a list of commands: {} and an example".format(
                sender, commands, example
            ),
            "data": "",
        }
    else:
        command = match.group()
        return {"found": True, "message": "valid command found", "data": command}


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


def resp_from_twillo_whatsapp(data):
    msg = data.get("Body")
    whatsapp_sender = data.get("From")
    sender = whatsapp_sender.split(":")[1]
    return {"msg": msg, "sender": sender}
