# Generated by Django 5.0.1 on 2024-05-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_orders_people_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='place',
            field=models.IntegerField(blank=True, default='-', null=True, verbose_name='Место'),
        ),
    ]
