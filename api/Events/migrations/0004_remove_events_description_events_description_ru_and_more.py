# Generated by Django 5.0.1 on 2024-04-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_rename_text_events_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='description',
        ),
        migrations.AddField(
            model_name='events',
            name='description_RU',
            field=models.TextField(default=545, verbose_name='Описание RU'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='description_UZ',
            field=models.TextField(default=544, verbose_name='Описание UZ'),
            preserve_default=False,
        ),
    ]
