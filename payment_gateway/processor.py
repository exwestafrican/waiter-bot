import request
from django.conf import settings

PAYSTACK_BASE_URL = "https://api.paystack.co/"


class PaymentProcessor:
    def __init__(self, *args, **kwargs):
        self.secret_key = settings.PAYSTACK_SECRET
        self.base_url = PAYSTACK_BASE_URL
        self.transfer_secret = settings.PAYSTACK_PAYOUT_SECRET

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