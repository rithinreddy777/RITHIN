# Generated by Django 4.0.4 on 2022-04-23 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
    ]
