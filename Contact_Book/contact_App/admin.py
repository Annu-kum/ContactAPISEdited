# Register your models here.
from django.contrib import admin

# Register your models here.
from contact_App.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('username','email',)
    #icon_name='add_circle'