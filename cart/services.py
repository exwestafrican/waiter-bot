from cart.models import *


def create_cart(owner, contact, bought_by, delivery_address, status):
    return Cart.objects.create(owner, contact, bought_by, delivery_address, status)


def create_cart_item(product, quantity, cart):
    return CartItem.objects.create(product=product, quantity=quantity, cart=cart)