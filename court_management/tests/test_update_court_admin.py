from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from authentication.models import User
from court_management.models import SurfaceType, CourtStatus, CourtType, Court


# Tests para actualizar cancha
class UpdateCourtTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
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
        self.court = Court.objects.create(
            name="Emerald Field",
            code="CZ501",
            size="20x40",
            location="1234 Evergreen Avenue, Springfield, Illinois",
            price_hour="100.00",
            description="Emerald Field is a premier sports facility located in Springfield, Illinois.",
            surface_type=self.surface_type,
            court_status=self.court_status,
            court_type=self.court_type
        )
        self.url = reverse('update_court_admin', args=[self.court.id])


    # Prueba exitosa
    def test_successfully(self):
        new_data = {
            'name': 'Updated Field',
            'code': 'CAS122',
            'size': '25x50',
            'location': '5678 Maple Street, Springfield, Illinois',
            'price_hour': '120.00',
            'description': 'Updated description of the field.',
            'surface_type': self.surface_type.id,
            'court_status': self.court_status.id,
            'court_type': self.court_type.id
        }
        response = self.client.put(self.url, data=new_data, format='json')        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba con datos inválidos
    def test_invalid_data(self):
        new_data = {
            'name': '',
            'code': 'CAS122',
            'size': '25x50',
            'location': '5678 Maple Street, Springfield, Illinois',
            'price_hour': '120.00',
            'description': 'Updated description of the field.',
            'surface_type': self.surface_type.id,
            'court_status': self.court_status.id,
            'court_type': self.court_type.id
        }
        response = self.client.put(self.url, data=new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)
    

    # Prueba con ID invalido
    def test_id_invalid(self):
        self.url = reverse('update_court_admin', args=[999])
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba sin autenticación
    def test_update_court_without_authentication(self):
        client = APIClient()
        response = client.put(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
