import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.mixins import TimeStampMixin

# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(
        max_length=15,
        null=True,
        help_text="user phone number e.g +23409050039030",
        unique=True,
    )


class Location(TimeStampMixin):
    area = models.CharField(
        max_length=800,
        null=True,
        help_text="locations are usually generic, like mainland or Ota",
    )

    state = models.CharField(
        max_length=600,
        help_text="lagos state",
    )

    popular_name = models.CharField(
        max_length=800,
        null=True,
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


class Restaurant(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=500,
        help_text="restaurant name",
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="who owns this restaurant",
    )

    address = models.OneToOneField(
        Location,
        help_text="where is your restaurant located",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    available_in = models.ManyToManyField(
        Location,
        related_name="available_in",
        help_text="where are the places this restruant is located in",
    )
    code = models.CharField(max_length=4, null=True, blank=True, unique=True)
    in_school = models.BooleanField(default=True)


class Profile(TimeStampMixin):
    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
        help_text="is this measured in scopes, or boxes or bottles",
    )

    def __str__(self):
        return "{}'s profile".format(self.user.first_name)

    @property
    def users_title(self):
        return self.user.groups.first()


# add a bank later on