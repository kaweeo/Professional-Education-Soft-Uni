# Generated by Django 5.0.6 on 2024-06-07 11:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "code",
                    models.CharField(
                        max_length=4, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "employee_count",
                    models.PositiveIntegerField(
                        default=1, verbose_name="Employee count"
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Sofia", "Sofia"),
                            ("Plovdiv", "Plovdiv"),
                            ("Burgas", "Burgas"),
                            ("Varna", "Varna"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("last_edit_on", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("email_address", models.EmailField(max_length=30)),
                ("photo", models.URLField()),
                ("birth_date", models.DateField()),
                ("works_full_name", models.BooleanField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]