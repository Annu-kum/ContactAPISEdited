from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class ContactBooks(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Email_Address = models.EmailField(max_length=200,unique=True,)
    Phone_Number = models.CharField(max_length=10,unique=True,validators=[RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits")])
