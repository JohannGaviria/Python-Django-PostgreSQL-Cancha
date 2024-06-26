from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from authentication.models import User
from court_management.models import SurfaceType, CourtStatus, CourtType


# Tests para crear cancha
class AddCourtTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('add_court_admin')
        self.admin_user = User.objects.create_superuser(
            full_name="test Admin",
            email="admin@example.com",
            password="adminpassword",
            phone="+57 301 203 4354",
            birth_date="1990-01-01"
        )
        self.client.force_authenticate(user=self.admin_user)
        self.court_status = CourtStatus.objects.create(status="Available")
        self.surface_type = SurfaceType.objects.create(type="Grass")
        self.court_type = CourtType.objects.create(type="Soccer")
        self.data = {
            "name": "Emerald Field",
            "code": "CZ501",
            "size": "20x40",
            "location": "1234 Evergreen Avenue, Springfield, Illinois",
            "price_hour": "100.00",
            "description": "Emerald Field is a premier sports facility located in Springfield, Illinois.",
            "surface_type": self.surface_type.id,
            "court_status": self.court_status.id,
            "court_type": self.court_type.id
        }
    

    # Prueba exitosa
    def test_successfully(self):
        response = self.client.post(self.url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba con datos inválidos
    def test_invalid_data(self):
        invalid_data = self.data.copy()
        invalid_data['name'] = ""
        response = self.client.post(self.url, data=invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba con código de cancha repetido
    def test_duplicate_code(self):
        response = self.client.post(self.url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        duplicate_data = self.data.copy()
        response = self.client.post(self.url, data=duplicate_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba sin autenticación
    def test_no_authentication(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)