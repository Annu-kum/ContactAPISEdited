from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient,APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from ..models import ContactBooks
from contact_App.models import User


class PostContactViewsTestCase(APITestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.access_token = AccessToken.for_user(self.user)
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'}

        ContactBooks.objects.create(Name="Annu",Email_Address="annu@gmail.com",Phone_Number="9343667527")
       # ContactBooks.objects.create(Name='Jane Smith', Email_Address='jane@example.com',Phone_Number="9343667827")
    def test_create_authenticted(self):
        url = reverse('createcontact')  
        data = {
            "Name": "John Doe",
            "Email_Address": "john@example.com",
            "Phone_Number":"9875345672",
        }
        response = self.client.post(url, data, format='json',**self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_unauthenticated(self):
        url=reverse('createcontact')
        data = {
            "Name":"Annu",
            "Email_Address":"annu@gmail.com",
            "Phone_Number":"8872345680"
        }
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

   