from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from authentication.models import User
from court_management.models import SurfaceType, CourtStatus, CourtType, Court


# Tests para eliminar cancha
class DeleteCourtTestCase(TestCase):
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
        self.url = reverse('delete_court_admin', args=[self.court.id])


    # Prueba exitosa
    def test_successfully(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba con ID invalido
    def test_id_invalid(self):
        self.url = reverse('delete_court_admin', args=[999])
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba sin autenticación
    def test_without_authentication(self):
        client = APIClient()
        response = client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

