# Generated by Django 5.0.2 on 2024-02-14 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactBooks',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Email_Address', models.CharField(max_length=200, unique=True)),
                ('Phone_Number', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]