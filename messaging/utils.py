import re


def find_command_in_message(msg):
    regex = r"^#\s?\w+"
    match = re.match(regex, msg)
    if not match:
        return {
            "found": False,
            "message": "No command found in message",
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
