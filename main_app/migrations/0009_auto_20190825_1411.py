# Generated by Django 2.1.5 on 2019-08-25 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20190824_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 25, 14, 10, 44, 116746), verbose_name='publishing date'),
        ),
    ]
