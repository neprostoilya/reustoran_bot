# Generated by Django 5.0.1 on 2024-05-10 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_orders_people_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='latitude',
            field=models.CharField(default='-', verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='orders',
            name='longitude',
            field=models.CharField(default='-', verbose_name='Долгота'),
        ),
    ]
