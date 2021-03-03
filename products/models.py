from django.db import models
import uuid
from utils.mixins import TimeStampMixin
from location.models import Store

# Create your models here.
class MeasurementType(TimeStampMixin):
    name = models.CharField(
        max_length=500, help_text="is this measured in scopes, or boxes or bottles"
    )

    def __str__(self):
        return self.name


class Category(TimeStampMixin):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Product(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500)
    base_charge = models.DecimalField(
        max_digits=9, decimal_places=2, help_text="how much does one unit of this cost"
    )
    addition_charge = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        help_text="how much does every additional unit charge",
    )
    measured_in = models.ForeignKey(
        MeasurementType,
        on_delete=models.SET_NULL,
        help_text="is this measured in scopes, or boxes or bottles",
        null=True,
        blank=True,
    )
    available = models.BooleanField(default=True)
    countable = models.BooleanField(default=True)
    sold_by = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name