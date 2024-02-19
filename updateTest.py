from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import ContactBooks
from rest_framework_simplejwt.tokens import AccessToken
from contact_App.models import User
from rest_framework import status

class ContactUpdateTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Annu', password='annu@123')
        self.access_token = AccessToken.for_user(self.user)
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'}
        # Create sample contact
        self.contact = ContactBooks.objects.create(Name="John Doe", Email_Address="john@example.com", Phone_Number="1234567890")

    def test_update_contact_authenticated(self):
        url = reverse('updatecontact', kwargs={'Name': self.contact.Name})
        data = {'Name': 'John Doe Updated', 'Email_Address': 'updated@example.com', 'Phone_Number': '9876543210'}
        response = self.client.put(url, data, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ContactBooks.objects.get(Name=data['Name']).Email_Address, 'updated@example.com')

    def test_update_contact_unauthenticated(self):
        url = reverse('updatecontact', kwargs={'Name': self.contact.Name})
        data = {'Name': 'John Doe Updated', 'Email_Address': 'updated@example.com', 'Phone_Number': '9876543210'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # contact remain since the request is unauthorized
        self.assertEqual(ContactBooks.objects.get(Name=self.contact.Name).Email_Address, 'john@example.com')
