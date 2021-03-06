from django.db import models
from products.models import Product
from utils.helper_func import add, subtract, multiply
from django.conf import settings
from utils.mixins import TimeStampMixin

import uuid

# Create your models here.


class OrderStatus(TimeStampMixin):
    name = models.CharField(max_length=500)


class Cart(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    contact = models.CharField(
        max_length=15,
        null=True,
        help_text="user phone number e.g +23409050039030",
    )
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    bought_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bought_by",
    )
    delivery_address = models.TextField()
    status = models.ForeignKey(
        OrderStatus, on_delete=models.SET_NULL, null=True, blank=True
    )
    reference = models.CharField(max_length=500, null=True, blank=True)
    fees = models.PositiveIntegerField(default=100)

    def __str__(self):
        if self.owner is not None:
            return "{}'s cart".format(self.owner.first_name)

        else:
            return "{}'s cart".format(self.contact)

    @property
    def from_school_vendor(self):
        try:
            return self.cart_item.first().product.sold_by.in_school
        except AttributeError:
            return None

    @property
    def items_total(self):
        products = self.cart_item.all()
        return sum([product.total for product in products])


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, null=True, blank=True, related_name="cart_item"
    )

    def __str__(self):
        return "{}'s {} of {}".format(
            self.quantity,
            self.product.measured_in.name,
            self.product,
        )

    @property
    def total(self):
        base_units = 1
        addition_units = float(self.quantity) - float(1)
        return multiply(base_units, self.product.base_charge) + multiply(
            addition_units, self.product.addition_charge
        )
