# Generated by Django 5.0.4 on 2024-07-24 08:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_book_isbn_alter_movie_director_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5, message='Author must be at least 5 characters long')]),
        ),
    ]