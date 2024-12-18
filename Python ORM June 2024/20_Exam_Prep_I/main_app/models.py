from django.core.validators import MinLengthValidator, MinValueValidator, MaxLengthValidator, MaxValueValidator
from django.db import models

from managers import DirectorManager
from mixins import MixinIsAwarded, MixinLastUpdated


# Create your models here.

class BaseModel(models.Model):
    class Meta:
        abstract = True

    full_name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )
    birth_date = models.DateField(
        default='1900-01-01',
    )
    nationality = models.CharField(
        max_length=50,
        default='Unknown',
    )


class Director(BaseModel):
    years_of_experience = models.SmallIntegerField(
        validators=[MinValueValidator(0)],
        default=0,
    )

    objects = DirectorManager()


class Actor(BaseModel, MixinIsAwarded, MixinLastUpdated):
    pass


class Movie(MixinIsAwarded, MixinLastUpdated):
    GENRE_CHOICES = (
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Other', 'Other'),
    )

    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)],
    )
    release_date = models.DateField()
    storyline = models.TextField(
        blank=True,
        null=True,
    )
    genre = models.CharField(
        max_length=6,
        choices=GENRE_CHOICES,
        default='Other',
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        default=0.0
    )
    is_classic = models.BooleanField(
        default=False,
    )
    director = models.ForeignKey(
        to=Director,
        on_delete=models.CASCADE,
        related_name='movies',
    )
    starring_actor = models.ForeignKey(
        to=Actor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movies'

    )
    actors = models.ManyToManyField(
        to=Actor,
        related_name='actor_movies'
    )
