from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from authentication.models import User
from court_management.models import CourtType


# Tests para crear/obtener tipos de cancha
class CourtTypeTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('court_type_admin')
        self.admin_user = User.objects.create_superuser(
            full_name="test Admin",
            email="admin@example.com",
            password="adminpassword",
            phone="+57 301 203 4354",
            birth_date="1990-01-01"
        )
        self.client.force_authenticate(user=self.admin_user)
        self.data = {
            "type": "basketball"
        }


    # Prueba obtener tipos de cancha
    def test_get_court_types(self):
        CourtType.objects.create(type='volleyball')
        CourtType.objects.create(type='basketball')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba crear tipo de cancha correctamente
    def test_create_valid_court_type(self):
        response = self.client.post(self.url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba crear tipo de cancha erroneamente
    def test_create_invalid_court_type(self):
        self.data['type'] = ""
        response = self.client.post(self.url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)

