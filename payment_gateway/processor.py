import requests
from django.conf import settings

PAYSTACK_BASE_URL = "https://api.paystack.co/"


class PaymentProcessor:
    def __init__(self, *args, **kwargs):
        self.secret_key = settings.PAYSTACK_SECRET
        self.base_url = PAYSTACK_BASE_URL

    def send_request(self, method, path, **kwargs):
        """
        Create a request stub
        :param method:
        :param path:
        :param kwargs:
        :return:
        """
        options = {
            "GET": requests.get,
            "POST": requests.post,
            "PUT": requests.put,
            "DELETE": requests.delete,
        }
        url = "{}{}".format(self.base_url, path)
        headers = {
            "content-type": "application/json",
            "Authorization": "Bearer {}".format(self.secret_key),
        }
        return options[method](url, headers=headers, **kwargs)

    def initialize_transaction(self, payload):
        response = self.send_request("POST", "transaction/initialize/", json=payload)
        return response.json()

    def verify_transaction(self, reference):
        # o2dmps2thb
        response = self.send_request("GET", "transaction/verify/{}/".format(reference))
        return response.json()
        # {
        #     "status": True,
        #     "message": "Authorization URL created",
        #     "data": {
        #         "authorization_url": "https://checkout.paystack.com/xnnkga0pmityg4b",
        #         "access_code": "xnnkga0pmityg4b",
        #         "reference": "o2dmps2thb",
        #     },
        # }

    def try_pri(self):
        print("prinngting")


payment_processor = PaymentProcessor()