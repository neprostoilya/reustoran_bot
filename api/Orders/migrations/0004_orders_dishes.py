# Generated by Django 5.0.1 on 2024-03-19 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0003_remove_dishes_jovy_dish_pk'),
        ('orders', '0003_alter_orders_datetime_selected'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='dishes',
            field=models.ManyToManyField(to='dishes.dishes', verbose_name='Блюда'),
        ),
    ]
