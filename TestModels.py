from rest_framework.test import APITestCase
from ..models import ContactBooks
from contact_App.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

#Test for models
class ContactAPITest(APITestCase):
    def setUp(self) :
        self.user=User.objects.create_user(username='Annu',password='annu@123')
        self.access_token = AccessToken.for_user(self.user)
        self.headers={'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'}

        #sample data...
        ContactBooks.objects.create(Name="kirti",Email_Address="kirti@gmail.com",Phone_Number="9688342490")
        ContactBooks.objects.create(Name="shusmita",Email_Address="shusmita@gmail.com",Phone_Number="8890456721")

    def test_get_authenticated(self):
        url=reverse('getcontact')
        response = self.client.get(url, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
#Test unauthentication...
    def test_get_unauthenticated(self):
        url=reverse('getcontact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_method(self):
        url='http://127.0.0.1:8000/contactAPI/getContact/'
        response=self.client.get(url,**self.headers)
        self.assertEqual(response.status_code,200)
        qs=ContactBooks.objects.filter(Name='kirti')
        qa=ContactBooks.objects.filter(Name='shusmita')
        self.assertEqual(qs.count(),1)
        self.assertEqual(qa.count(),1)

