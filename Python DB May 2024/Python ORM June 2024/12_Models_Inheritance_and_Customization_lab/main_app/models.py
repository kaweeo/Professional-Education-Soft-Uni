from datetime import date

from django.core.exceptions import ValidationError
from django.db import models


# 07. Veterinarian Availability
class BooleanChoiceField(models.BooleanField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = (
            (True, 'Available'),
            (False, 'Not Available')
        )
        kwargs['default'] = True
        super().__init__(*args, **kwargs)


# 01. Zoo Animals
class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)

    # 06. Animal's Age
    @property
    def age(self):
        today = date.today()
        age = today - self.birth_date

        return age.days // 365


class Mammal(Animal):
    fur_color = models.CharField(max_length=50)


class Bird(Animal):
    wing_span = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )


class Reptile(Animal):
    scale_type = models.CharField(max_length=50)


# 02. Zoo Employees

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    # Turns the model into an Abstract Base Class
    class Meta:
        abstract = True


# class ZooKeeper(Employee):
#     SPECIALTY_CHOICES = (
#         ("Mammals", "Mammals"),
#         ("Birds", "Birds"),
#         ("Reptiles", "Reptiles"),
#         ("Others", "Others")
#     )
#     specialty = models.CharField(max_length=10, choices=SPECIALTY_CHOICES)
#     managed_animals = models.ManyToManyField(to=Animal)


class ZooKeeper(Employee):
    class Speciality(models.TextChoices):
        Mammals = 'Mammals'
        Birds = 'Birds'
        Reptiles = 'Reptiles'
        Others = 'Others'

    specialty = models.CharField(
        max_length=10,
        choices=Speciality.choices
    )
    managed_animals = models.ManyToManyField(
        to=Animal
    )

    # 04. Zookeeper's Specialty
    def clean(self):
        # Call the clean method of the parent class
        # check for other validations
        super().clean()  # is called to ensure any validation logic defined in the parent class is also executed

        # Custom validation logic, clean method is before saving the data in db
        # it checks is data valid
        if self.specialty not in self.Speciality:
            raise ValidationError('Specialty must be a valid choice.')


class Veterinarian(Employee):
    license_number = models.CharField(max_length=10)

    # 07. Veterinarian Availability
    availability = BooleanChoiceField()


# 03. Animal Display System
class ZooDisplayAnimal(Animal):
    class Meta:
        proxy = True

    # 05. Animal Display System Logic
    def display_info(self):
        return f"Meet {self.name}! Species: {self.species}, born {self.birth_date}. " \
               f"It makes a noise like '{self.sound}'."

    def is_endangered(self):
        animals_at_risk = ["Cross River Gorilla", "Orangutan", "Green Turtle"]
        if self.species in animals_at_risk:
            return f"{self.species} is at risk!"

        return f"{self.species} is not at risk."
