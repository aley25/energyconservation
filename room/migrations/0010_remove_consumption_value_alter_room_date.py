# Generated by Django 4.0.1 on 2022-01-05 03:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0009_consumption_value_alter_room_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumption',
            name='value',
        ),
        migrations.AlterField(
            model_name='room',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 4, 21, 50, 56, 143008)),
        ),
    ]
