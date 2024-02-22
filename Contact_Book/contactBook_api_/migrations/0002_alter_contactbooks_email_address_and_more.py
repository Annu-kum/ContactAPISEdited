# Generated by Django 5.0.2 on 2024-02-17 10:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactBook_api_', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactbooks',
            name='Email_Address',
            field=models.EmailField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='contactbooks',
            name='Phone_Number',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^\\d{10}$', message='Phone number must be 10 digits')]),
        ),
    ]