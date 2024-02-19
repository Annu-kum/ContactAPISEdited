from rest_framework.test import APITestCase
from rest_framework import status
from ..models import ContactBooks
from rest_framework_simplejwt.tokens import AccessToken
from contact_App.models import User

class ContactIntegrationTestCase(APITestCase):
    def setUp(self):    
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.access_token=AccessToken.for_user(self.user)
        self.headers={'HTTP_AUTHORIZATION':f'Bearer {self.access_token}'}
        
# Test to post the data...    
    def test_create_contact(self):
        url = 'http://127.0.0.1:8000/contactAPI/postContact/' 
        data = {
            "Name": "John Doe",
            "Email_Address": "john@example.com",
            "Phone_Number":"9834567890"
        }
        response = self.client.post(url, data, format='json',**self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#Test to get the data...
    def test_list_contacts(self):
        ContactBooks.objects.create(Name="John Doe", Email_Address="john@example.com",Phone_Number="9834567890")
        
        url=f'http://127.0.0.1:8000/contactAPI/getContact/'
        response = self.client.get(url, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#Test to update the data...
    def test_update_contact(self):
        contact = ContactBooks.objects.create(Name="John Doe", Email_Address="john@example.com", Phone_Number="9834567890")
        
        urls=f'http://127.0.0.1:8000/contactAPI/update/{contact.Name}/'
        
        new_data = {"Name": "John Smith", "Email_Address": "john@example.com", "Phone_Number": "9884567890"}
        response = self.client.put(urls, new_data, format='json',kwargs={'name': contact.Name}, **self.headers)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        contact.refresh_from_db()
        self.assertEqual(contact.Name, "John Smith")
        self.assertEqual(contact.Email_Address, "john@example.com")
        self.assertEqual(contact.Phone_Number, "9884567890")

#Test to delete the data...
    def test_delete_contact(self): 
        contact = ContactBooks.objects.create(Name="John Doe", Email_Address="john@example.com",Phone_Number="9834567890")
        
        url = f'http://127.0.0.1:8000/contactAPI/delete/{contact.Name}/' 
        response = self.client.delete(url,**self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(ContactBooks.objects.filter(Name="John Doe").exists())
