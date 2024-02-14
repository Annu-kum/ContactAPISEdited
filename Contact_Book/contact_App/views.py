from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User




class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create your views here.


