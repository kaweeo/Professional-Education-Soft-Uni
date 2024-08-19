from django.core.validators import MinLengthValidator
from django.db import models
from .validators import OnlyLettersValidator


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2), OnlyLettersValidator
        ],
        unique=True,
        null=False,
        blank=False
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False
    )

    nutriotion = models.TextField(
        null=True,
        blank=True
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        null=True,
    )
