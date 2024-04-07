# Generated by Django 5.0.1 on 2024-04-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0004_remove_dishes_description_remove_dishes_title_and_more'),
        ('orders', '0008_remove_orders_dishes_dishesorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='dish',
            field=models.ManyToManyField(to='dishes.dishes', verbose_name='Блюдо'),
        ),
        migrations.DeleteModel(
            name='DishesOrder',
        ),
    ]