# Generated by Django 3.0.3 on 2020-07-12 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 12, 18, 57, 0, 865833), verbose_name='date published'),
        ),
    ]
