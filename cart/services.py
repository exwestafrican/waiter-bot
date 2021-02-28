from cart.models import *


def create_cart(owner, contact, bought_by, delivery_address, status):
    return Cart.objects.create(
        owner=owner,
        contact=contact,
        bought_by=bought_by,
        delivery_address=delivery_address,
        status=status,
    )


def create_cart_item(product, quantity, cart):
    return CartItem.objects.create(product=product, quantity=quantity, cart=cart)