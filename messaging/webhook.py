from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from messaging.twilio_whatsapp import send_whatsapp_message
from twilio.twiml.messaging_response import MessagingResponse

from django.http import HttpResponse


@api_view(["POST"])
def message_received(request):
    if request.method == "POST":
        print("received message", request.data.get("Body"))
        # send_whatsapp_message(
        #     "+2348169084566",
        #     "+14155238886",
        #     "got the message" + str(request.data.get("ProfileName")),
        # )
        response = MessagingResponse()
        msg = response.message("Send us an image!" + request.data.get("Body"))
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
