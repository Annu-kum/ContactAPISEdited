from rest_framework import serializers
from .models import ContactBooks


class contactBookSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=ContactBooks
        fields= ['Name','Email_Address','Phone_Number']