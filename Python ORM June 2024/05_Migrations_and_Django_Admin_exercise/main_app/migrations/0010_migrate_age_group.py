# Generated by Django 5.0.4 on 2024-06-20 10:16

from django.db import migrations


def set_age_group(apps, schema_editor):
    person_model = apps.get_model('main_app', 'Person')

    persons = person_model.objects.all()

    for person_record in persons:
        if person_record.age <= 12:
            person_record.age_group = 'Child'
        elif person_record.age <= 17:
            person_record.age_group = 'Teen'
        else:
            person_record.age_group = 'Adult'

    person_model.objects.bulk_update(persons, ['age_group'])


def set_age_group_default(apps, schema_editor):
    person_model = apps.get_model('main_app', 'Person')

    # Get field default value from _meta
    age_group_default = person_model._meta.get_field("age_group").default

    for person in person_model.objects.all():
        person.age_group = age_group_default
        person.save()



class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0009_person'),
    ]

    operations = [
        migrations.RunPython(set_age_group, reverse_code=set_age_group_default)
    ]
