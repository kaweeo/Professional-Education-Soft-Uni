from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Student №{self.student_id}: {self.first_name} {self.last_name}; Email: {self.email}"