from django.core.validators import MinValueValidator
from django.db import models
from django.utils import choices
from albums.choices import GenreChoices
from profiles.models import Profile


class Album(models.Model):
    album_name = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        null=False,
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=GenreChoices.choices,  # This populates the choices for the field with the options
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(0.0),
        ],
    )

    owner = models.ForeignKey(
        # to=Profile,
        to='profiles.Profile', # When defining relationships between models in different apps.
        on_delete=models.CASCADE,
        related_name='albums',
    )
