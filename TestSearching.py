from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
from ..models import ContactBooks
from contact_App.models import User


class SearchContactTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.access_token = AccessToken.for_user(self.user)
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'}

        # Create  ContactBooks instances for testing
        self.contact1= ContactBooks.objects.create(Name="John Doe", Email_Address="john@example.com",Phone_Number="9383667527")
        self.contact2= ContactBooks.objects.create(Name="Jane Doe", Email_Address="jane@example.com",Phone_Number="9343667525")
        self.contact3=ContactBooks.objects.create(Name="Alice Smith", Email_Address="alice@example.com",Phone_Number="9343667557")
    
    
    def test_list_contacts(self):
        url = reverse('getcontact')  
        response = self.client.get(url, **self.headers)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['Name'], 'John Doe')
        self.assertEqual(response.data[0]['Email_Address'], 'john@example.com')
        self.assertEqual(response.data[1]['Name'], 'Jane Smith')
        self.assertEqual(response.data[1]['Email_Address'], 'jane@example.com')



    def test_search_contact_by_name(self):

        url = reverse('getcontact')  
        response = self.client.get(url, {'search': 'Doe'}, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)
        self.assertIn("John Doe", [contact['Name'] for contact in response.data])
        self.assertIn("Jane Doe", [contact['Name'] for contact in response.data])

    def test_search_contact_by_email(self):
        url = reverse('getcontact')  
        response = self.client.get(url, {'search': 'example.com'}, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 3)
        self.assertIn("john@example.com", [contact['Email_Address'] for contact in response.data])
        self.assertIn("jane@example.com", [contact['Email_Address'] for contact in response.data])
        self.assertIn("alice@example.com", [contact['Email_Address'] for contact in response.data])

