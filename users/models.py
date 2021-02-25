import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from users.validators import validate_mobile_number

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(
        max_length=15,
        null=True,
        validators=[validate_mobile_number],
        help_text="user phone number e.g +23409050039030",
        unique=True,
    )