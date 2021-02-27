from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from messaging.twilio_whatsapp import send_whatsapp_message
from twilio.twiml.messaging_response import MessagingResponse

from django.http import HttpResponse

from commands.selectors import command_list

from messaging.utils import clean_data, find_command


@api_view(["POST"])
def message_received(request):
    if request.method == "POST":
        msg = request.data.get("Body")
        sender = request.data.get("From")
        message = clean_data(msg)
        response = MessagingResponse()
        command = find_command(msg)
        if command:
            handle_command()
        else:
            response.message(
                "hey, {} we can't figure out what you want, but here are a list of commands: "
            )
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
