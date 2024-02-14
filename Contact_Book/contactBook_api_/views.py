from django.shortcuts import render
from rest_framework import viewsets  
# Create your views here.
from .models import ContactBooks
from .Serializers import contactBookSerializers
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class PageNumberPaginations(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 100
    

# contactBook viewset 
class ContactViewset(viewsets.ModelViewSet):
    queryset = ContactBooks.objects.all()
    serializer_class = contactBookSerializers
    authentication_classes = [JWTAuthentication]  #for authentication
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter] #for search Through Name & Email
    search_fields = ['Name','Email_Address']
    pagination_class = PageNumberPaginations # For the pagination of 10