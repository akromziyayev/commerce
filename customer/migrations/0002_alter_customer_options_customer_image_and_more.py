# Generated by Django 5.0.6 on 2024-06-22 19:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ('-joined',), 'verbose_name_plural': 'Customers'},
        ),
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='customer/customer_img'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='full_name',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name="to'liq ismi"),
        ),
        migrations.AlterField(
            model_name='customer',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 22, 12, 2, 43, 276796)),
        ),
    ]
