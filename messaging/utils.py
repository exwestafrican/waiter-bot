import re
from commands.selectors import get_command_list, get_example, get_a_random_command


def find_command_in_message(msg, sender):
    regex = r"#\s?\w+"
    match = re.findall(regex, msg)
    print(match)
    if not match:
        commands = ", ".join(get_command_list()[:5])
        command = get_a_random_command()
        example = get_example(command)
        # send example link
        return {
            "found": False,
            "message": "Hey, {} we couldn't find any command in your message, here are a list of commands to try from: {}. Check this example out {}".format(
                sender, commands, example
            ),
            "data": "",
        }
    else:
        command = match[0].split("#")[1]
        return {"found": True, "message": "valid command found", "data": command}


def clean_data(data):
    return data.strip().lower()


def handle_command(command):
    # call a service
    pass


def resp_from_twillo_whatsapp(data):
    msg = data.get("Body")
    whatsapp_sender = data.get("From")
    sender = whatsapp_sender.split(":")[1]
    return {"msg": msg, "sender": sender}
