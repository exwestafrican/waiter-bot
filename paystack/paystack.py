BASE_URL = "https://api.paystack.co/"
import request

class PaymentProcessor:
    def initialize_transaction(self, payload):
        url = "{}transaction/initialize".format{BASE_URL}
        request.post(url)
        pass