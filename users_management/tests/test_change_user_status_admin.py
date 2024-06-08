from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from authentication.models import User, Rol


# Tests para activar/desactivar usuario
class ChangeUserStatusTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            full_name="test fullname",
            email="test@email.com",
            password="testpassword",
            phone="+57 321 543 7665",
            birth_date="1999-09-09",
            rol=Rol.objects.create(rol='user')
        )
        self.admin_user = User.objects.create_superuser(
            full_name="test Admin",
            email="admin@example.com",
            password="adminpassword",
            phone="+57 301 203 4354",
            birth_date="1990-01-01"
        )
        self.client.force_authenticate(user=self.admin_user)
        self.url = reverse('change_user_status_admin', args=[self.user.id])
        self.data = {
            'action': 'activate'
        }


    # Prueba activar usuario exitosa
    def test_activate_user_successful(self):
        response = self.client.patch(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertTrue(self.user.is_active)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba desactivar usuario exitosa
    def test_deactivate_user_successful(self):
        self.data['action'] = 'deactivate'
        response = self.client.patch(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertFalse(self.user.is_active)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba activar/desactivar con parámetro incorrecto
    def test_change_user_status_invalid_action(self):
        self.data['action'] = 'invalid_action'
        response = self.client.patch(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba no existe usuario
    def test_change_status_user_not_found(self):
        url = reverse('change_user_status_admin', args=[12345])
        response = self.client.patch(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba sin autenticación
    def test_change_status_unauthenticated(self):
        self.client = APIClient()
        response = self.client.patch(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
