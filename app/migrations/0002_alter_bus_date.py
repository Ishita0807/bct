# Generated by Django 5.1 on 2024-08-10 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 10, 12, 26, 20, 320020, tzinfo=datetime.timezone.utc)),
        ),
    ]
