from twilio.rest import Client
from django.conf import settings


def send_text_message(to, message):
    """
    sends text message to a user
    """

    client = Client(settings.ACCOUNT_SID, settings.ACCOUNT_TOKEN)
    message = client.messages.create(
        to=to,
        from_="+14702214016",
        body=message,
    )
    return {"status": "OK", "message": message}
