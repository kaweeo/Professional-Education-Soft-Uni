# Generated by Django 5.0.4 on 2024-06-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_merge_0011_item_0012_migrate_item_rarity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('category', models.CharField(default='empty', max_length=20)),
            ],
        ),
    ]