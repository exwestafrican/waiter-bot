from cart.models import *
from cart.selectors import get_order_status


def create_cart(owner, contact, email, bought_by, delivery_address, status="pending"):
    return Cart.objects.create(
        owner=owner,
        contact=contact,
        email=email,
        bought_by=bought_by,
        delivery_address=delivery_address,
        status=get_order_status(name=status),
    )


def create_cart_item(product, quantity, cart):
    return CartItem.objects.create(product=product, quantity=quantity, cart=cart)