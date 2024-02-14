from django.db import models

# Create your models here.
class ContactBooks(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Email_Address = models.CharField(max_length=200,unique=True)
    Phone_Number = models.CharField(max_length=10,unique=True)
