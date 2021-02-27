from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from twilio.twiml.messaging_response import MessagingResponse


from commands.selectors import command_list
from commands.selectors import get_command_list, get_example
from messaging.twilio_whatsapp import send_whatsapp_message
from messaging.utils import clean_data, find_command, resp_from_twillo_whatsapp


@api_view(["POST"])
def message_received(request):
    if request.method == "POST":
        resp = resp_from_twillo_whatsapp(request.data)
        msg = resp["msg"]
        sender = resp["sender"]
        message = clean_data(msg)
        response = MessagingResponse()

        command = find_command(msg)
        if command:
            pass
            # handle_command()
            response.message(
                "hey, {} we're working on this, give us a minute".format(sender)
            )
        else:
            commands = ", ".join(get_command_list())
            example = get_example(commands[0])
            response.message(
                "hey, {} we can't figure out what you want, but here are a list of commands: {}, to use one, simply do {}".format(
                    sender, commands, example
                )
            )
            print(response)
        # "#order rice-50,plantain-70,meat-50"
        # send_whatsapp_message(
        #     "+2348169084566",
        #     "+14155238886",
        #     "got the message" + str(request.data.get("ProfileName")),
        # )

        return HttpResponse(str(response))


@api_view(["POST"])
def send_message(request):
    if request.method == "POST":
        print("sending")
        msg = request.data.get("message", "trials")
        sent = send_whatsapp_message("+2348169084566", "+14155238886", msg)
        return Response(
            {"success": True, "message": "success", "data": sent},
            status=status.HTTP_200_OK,
        )
