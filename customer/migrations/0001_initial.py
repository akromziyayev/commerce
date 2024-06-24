# Generated by Django 5.0.6 on 2024-06-22 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=155, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=150)),
                ('joined', models.DateTimeField(default=datetime.datetime(2024, 6, 22, 11, 22, 49, 745509))),
            ],
        ),
    ]
