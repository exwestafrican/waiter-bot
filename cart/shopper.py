from cart.models import *

from cart.selectors import (
    get_order_status,
    get_quantity_ordered,
    validate_quantity_ordered,
)

from products.selectors import product_is_valid
from users.selectors import get_user
from utils.helper_func import subtract, add, multiply
from utils.constants import *

from cart.utils import whole_number


class Shopper:
    def __init__(self, number, cart, *args, **kwargs):
        self.cart = cart
        self.number = number

    @classmethod
    def start_shopping(cls, number):
        owner = get_user(phone_number=number)
        cart = create_cart(
            owner=owner,
            contact=number,
            bought_by=None,
            delivery_address="",
            status=get_order_status(name=PENDING),
        )
        return cls(number, cart)

    def add_item_to_cart(self, product, amount):
        valid = True
        valid_quantity = validate_quantity_ordered(product, amount)
        product_is_valid = product_is_valid(product)
        if product_is_valid and valid_quantity is valid:
            quantity = get_quantity_ordered(product, amount_paid)
            create_cart_item(product, quantity, self.cart)
        else:
            pass

    def confirm_order(self, address: str):
        self.cart.address = address
        self.cart.status = get_order_status(name=CONFIRMED)
        return cart.save()

    def cancled_order(self):
        self.cart.status = get_order_status(name=CANCLED)
        return cart.save()

    @classmethod
    def get_pending_order(number):
        pending_orders = Cart.objects.first(
            number=number, status__title=PENDING
        ).order_by("-created_at")
        most_recent_order = pending_orders[0]
        return most_recent_order
