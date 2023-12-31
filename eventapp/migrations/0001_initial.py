# Generated by Django 4.0.4 on 2022-04-23 09:04

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('eventdate', models.DateField()),
                ('place', models.CharField(max_length=40, null=True)),
                ('status', models.CharField(default='Scheduled', max_length=20)),
                ('maxcapacity', models.IntegerField()),
                ('photo', models.ImageField(default='noimage.png', upload_to='pics')),
                ('createdon', models.DateTimeField(auto_now=True)),
                ('isavailable', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'events',
                'ordering': ['-eventid'],
            },
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('unit', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'fooditems',
                'ordering': ['-fid'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=50)),
                ('pwd', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('gender', models.CharField(max_length=12, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('isadmin', models.BooleanField(default=False)),
                ('createdon', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
                'ordering': ['-createdon'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('fooditems', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('book_date', models.DateField()),
                ('status', models.CharField(default='Pending', max_length=30)),
                ('userstatus', models.CharField(max_length=20, null=True)),
                ('createdon', models.DateTimeField(auto_now=True)),
                ('cardno', models.CharField(max_length=16)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('progress', models.DecimalField(decimal_places=2, max_digits=5)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.user')),
            ],
            options={
                'db_table': 'bookings',
                'ordering': ['-bid'],
            },
        ),
    ]
