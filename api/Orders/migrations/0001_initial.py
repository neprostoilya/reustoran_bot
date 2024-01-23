# Generated by Django 5.0.1 on 2024-01-23 08:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Dishes', '0003_alter_dishes_options_alter_dishes_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Имя')),
                ('surname', models.CharField(verbose_name='Фамилия')),
                ('phone', models.CharField(verbose_name='Номер')),
                ('datetime', models.DateTimeField(verbose_name='Дата')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dishes.dishes', verbose_name='Блюдо')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
