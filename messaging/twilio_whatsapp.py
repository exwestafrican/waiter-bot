from twilio.rest import Client

account_sid = "AC7309047decd3d7588c27ae5c8e47fb6c"
auth_token = "[AuthToken]"
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="whatsapp:+14155238886",
    body="Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/",
    to="whatsapp:+2348169084566",
)
