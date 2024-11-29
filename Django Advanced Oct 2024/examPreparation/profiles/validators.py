import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CustomUsernameValidator:
    def __init__(self):
        pass

    def __call__(self, value: str, *args, **kwargs):
        if not re.match(r'^[\w]+$', value):  # \w matches [a-zA-Z0-9_]
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")

        # No return True is needed, Validators are void