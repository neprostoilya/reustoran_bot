# Generated by Django 5.0.1 on 2024-02-15 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carts',
            old_name='amount',
            new_name='quantity',
        ),
    ]
