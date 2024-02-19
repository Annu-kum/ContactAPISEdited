from rest_framework.test import APITestCase
from rest_framework import status
from ..models import ContactBooks
from contact_App.models import User
from rest_framework_simplejwt.tokens import AccessToken

#Test for deletion...
class ContactViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Annu', password='annu@123')
        self.access_token = AccessToken.for_user(self.user)
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'}
        

    def test_delete_authenticated(self): 
       contact= ContactBooks.objects.create(Name="JohnDoe", Email_Address="john@example.com", Phone_Number="1234567890")  
       url= f'http://127.0.0.1/contactAPI/delete/{contact.Name}/'
       response = self.client.delete(url, **self.headers)
       self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_unauthenticated(self):
       url= 'http://127.0.0.1/contactAPI/delete/JohnDoe/'
       response = self.client.delete(url)
       self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
       