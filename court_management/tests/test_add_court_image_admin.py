from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from authentication.models import User
from court_management.models import SurfaceType, CourtStatus, CourtType, Court


# Tests para agregar imágenes de la cancha
class AddCourtImageTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('add_court_image_admin')
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
        self.image = SimpleUploadedFile(
            name='test_image.jpg',
            content=open('uploads/test_image_1.jpg', 'rb').read(),
            content_type='image/jpeg'
        )
        self.data = {
            'image': self.image,
            'court': self.court.id
        }


    # Prueba exitosa
    def test_successfully(self):
        response = self.client.post(self.url, data=self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba con datos inválidos
    def test_invalid_data(self):
        invalid_data = self.data.copy()
        invalid_data['image'] = SimpleUploadedFile(name='test_image.txt', content=b'invalid image content', content_type='text/plain')
        response = self.client.post(self.url, data=invalid_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba con cancha que no existe
    def test_invalid_court(self):
        invalid_data = self.data.copy()
        invalid_data['court'] = 999
        response = self.client.post(self.url, data=invalid_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba sin autenticación
    def test_no_authentication(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url, data=self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
