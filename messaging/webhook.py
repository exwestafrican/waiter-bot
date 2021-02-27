from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from twilio.twiml.messaging_response import MessagingResponse


from commands.selectors import command_list
from commands.selectors import get_command_list, get_example
from messaging.twilio_whatsapp import send_whatsapp_message
from messaging.utils import clean_data, resp_from_twillo_whatsapp
from messaging.selectors import get_name_or_number, valid_command_in_message


@api_view(["POST"])
def message_received(request):
    if request.method == "POST":
        resp = resp_from_twillo_whatsapp(request.data)
        msg = resp["msg"]
        sender = get_name_or_number(resp["sender"])
        message = clean_data(msg)
        response = MessagingResponse()
        procees_message = valid_command_in_message(message)
        if procees_message.get("success"):
            response.message(
                "hey, {} your order with id 2234 has been created".format(sender)
            )
        else:
            response.message(procees_message.get("message"))

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
