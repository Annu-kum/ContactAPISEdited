from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .models import ContactBooks
from .Serializers import contactBookSerializers
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

#Pagination code...
class PageNumberPaginations(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    max_page_size=100

    

# contactBook viewset 
class GetViewset(generics.ListAPIView):
   #Get contact... 
    queryset = ContactBooks.objects.all().order_by('Name')
    serializer_class = contactBookSerializers
    pagination_class = PageNumberPaginations
    authentication_classes = [JWTAuthentication]  #for authentication
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter] #for search Through Name & Email
    search_fields = ['Name','Email_Address']
    
class Postcontactviews(generics.CreateAPIView,generics.ListAPIView):
    #Get and Create contact...
    queryset = ContactBooks.objects.all().order_by('Name')
    serializer_class = contactBookSerializers
    pagination_class = PageNumberPaginations
    authentication_classes = [JWTAuthentication]  #for authentication
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter] #for search Through Name & Email
    search_fields = ['Name','Email_Address']

class deletecontactviews(generics.DestroyAPIView,generics.ListAPIView):
    #Get and Delete contact...
    queryset = ContactBooks.objects.all().order_by('Name')
    serializer_class = contactBookSerializers
    pagination_class = PageNumberPaginations
    authentication_classes = [JWTAuthentication]  #for authentication
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter] #for search Through Name & Email
    search_fields = ['Name','Email_Address']

    def destroy(self, request, *args, **kwargs):
        name = kwargs.get('name', None)
        if name:
            try:
                contact = ContactBooks.objects.get(Name=name)
                contact.delete()
                return Response({'message': 'Contact deleted successfully'}, status=status.HTTP_200_OK)
            except ContactBooks.DoesNotExist:
                return Response({'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Name parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

class updatecontactviews(generics.UpdateAPIView,generics.ListAPIView):
    #Get and update the contact...
    queryset = ContactBooks.objects.all().order_by('Name')
    serializer_class = contactBookSerializers
    pagination_class = PageNumberPaginations
    authentication_classes = [JWTAuthentication]  #for authentication
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter] #for search Through Name & Email
    search_fields = ['Name','Email_Address']
    lookup_field = 'Name'  # Specify the field to use for lookup

   