from django.db import models

# Create your models here.
import uuid
from django.db import models
from utils.mixins import TimeStampMixin
from django.conf import settings


class Location(TimeStampMixin):
    area = models.CharField(
        max_length=800,
        help_text="locations are usually generic, like mainland or Ota",
    )

    state = models.CharField(
        max_length=600,
        help_text="lagos state",
    )

    popular_name = models.CharField(
        max_length=800,
        null=True,
        blank=True,
        help_text="where do people usually attribute this place to",
    )

    def __str__(self):
        return "{},{}".format(self.area, self.state)

    @property
    def generic_address(self):
        return "{} ({})".format(self.area, self.popular_name)

    @property
    def location_zip(self):
        return self.pk


class Store(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=500,
        help_text="restaurant name",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text="who owns this restaurant",
    )

    address = models.TextField(
        help_text="where is your restaurant located",
    )

    available_in = models.ManyToManyField(
        Location,
        related_name="available_in",
        help_text="where are the places this restruant is located in",
    )
    code = models.CharField(max_length=4, null=True, blank=True, unique=True)
    in_school = models.BooleanField(default=True)
