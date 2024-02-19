from django.test import TestCase
from ..Serializers import contactBookSerializers

class ContactBookSerializerTestCase(TestCase):
    def test_valid_serializer(self):
        data = {'Name': 'John Doe', 'Email_Address': 'john@example.com', 'Phone_Number': '1234567890'}
        serializer = contactBookSerializers(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer(self):
        data = {'Name': 'Jane Doe', 'Phone_Number': '9876543210'}  # Missing Email_Address
        serializer = contactBookSerializers(data=data)
        self.assertFalse(serializer.is_valid())