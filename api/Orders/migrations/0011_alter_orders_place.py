# Generated by Django 5.0.1 on 2024-05-09 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_remove_orders_type_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='place',
            field=models.CharField(blank=True, default='-', null=True, verbose_name='Место'),
        ),
    ]
