from twilio.rest import Client
from conf.base import ACCOUNT_SID, ACCOUNT_TOKEN


account_sid = ACCOUNT_SID
auth_token = ACCOUNT_TOKEN

client = Client(account_sid, auth_token)


def send_whatsapp_message(to, from_, message):
    message = client.messages.create(
        from_="whatsapp:{}".format(from_),
        body=message,
        to="whatsapp:{}".format(to),
    )
