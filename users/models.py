import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.mixins import TimeStampMixin
from django.conf import settings

# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(
        max_length=15,
        null=True,
        help_text="user phone number e.g +23409050039030",
        unique=True,
    )


class ActivityLog(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="activity_logger",
    )
    action = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    successful = models.BooleanField(default=True)

    def __str__(self):
        return self.action


class Profile(TimeStampMixin):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
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