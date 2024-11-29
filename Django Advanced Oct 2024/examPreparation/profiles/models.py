from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from profiles.validators import CustomUsernameValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,  # max_length here is must, because of CharField
        validators=[  # can not be implemented w MaxLengthValidator only
            MinLengthValidator(2),
            CustomUsernameValidator(),
        ]
    )

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True
    )

    age = models.IntegerField(
        null=True,
        blank=True,
    )

