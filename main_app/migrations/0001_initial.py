# Generated by Django 2.1.5 on 2019-08-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(verbose_name='publishing date')),
            ],
        ),
    ]
