from django.db import models
from products.models import Product
from utils.helper_func import add, subtract, multiply
from django.conf import settings
from utils.mixins import TimeStampMixin

import uuid

# Create your models here.


class OrderStatus(TimeStampMixin):
    name = models.CharField(max_length=500)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({} {}}".format(
            self.product.name, self.quantity, self.product.measured_in
        )

    @property
    def total(self):
        base_units = 1
        addition_units = subtract(self.quantity, 1)
        return multiply(base_units, self.product.base_charge) + multiply(
            addition_units, self.product.addition_charge
        )


class Cart(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart_item = models.ForeignKey(
        CartItem, on_delete=models.SET_NULL, null=True, blank=True
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    contact = models.CharField(
        max_length=15,
        null=True,
        help_text="user phone number e.g +23409050039030",
        unique=True,
    )
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

    def __str__(self):
        if self.owner is not None:
            return "{}'s cart".format(self.owner.first_name)

        else:
            return "{}'s cart".format(self.contact)
