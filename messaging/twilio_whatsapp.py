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


send_whatsapp_message("+2348169084566", "+14155238886", "working?")

# message = client.messages.create(
#     from_="whatsapp:+14155238886",
#     body="Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/",
#     to="whatsapp:+2348169084566",
# )
