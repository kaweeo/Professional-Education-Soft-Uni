# Generated by Django 5.0.4 on 2024-06-20 17:23

from django.db import migrations
from django.utils import timezone


def set_warranty(apps, schema_editor):
    orders_model = apps.get_model('main_app', 'Order')
    orders = orders_model.objects.all()

    for order in orders:
        if order.status == "Pending":
            order.delivery = order.order_date + timezone.timedelta(days=3)
            order.save()
        elif order.status == "Completed":
            order.warranty = "24 months"
            order.save()
        elif order.status == "Cancelled":
            order.delete()


def reverse_delivery_and_warranty(apps, schema):
    orders_model = apps.get_model('main_app', 'Order')
    orders = orders_model.objects.all()

    for order in orders:
        if order.status == "Pending":
            order.delivery = None
        elif order.status == "Completed":
            order.warranty = "No warranty"

        order.save()


class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0016_order'),
    ]

    operations = [
        migrations.RunPython(set_warranty, reverse_code=reverse_delivery_and_warranty)
    ]