from django.contrib import admin

# Register your models here.
from contactBook_api_.models import ContactBooks

@admin.register(ContactBooks)
class ContactAdmin(admin.ModelAdmin):
    list_display=('Name','Email_Address','Phone_Number')