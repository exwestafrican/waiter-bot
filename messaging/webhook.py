from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from messaging.twilio_whatsapp import send_whatsapp_message


@api_view(["POST"])
def message_received(request):
    if request.method == "POST":
        print("received message", request.data)
        send_whatsapp_message("+2348169084566", "+14155238886", "got the message")
        return Response(
            {"success": True, "message": "success", "data": "none"},
            status=status.HTTP_200_OK,
        )


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
