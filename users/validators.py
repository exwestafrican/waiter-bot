import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_mobile_number(number:str):
    regex = r"^\+234\d{10}$"
    match = re.match(regex,number)
    if not match:
        raise ValidationError(
            _('%(number) is not a valid phone number'),
            params={'number': number},
        )
