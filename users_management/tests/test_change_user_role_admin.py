from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from authentication.models import User, Rol


# Tests para cambiar el rol del usuario
class ChangeUserRoleTestCase(TestCase):
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
        self.url = reverse('change_user_role_admin', args=[self.user.id])
        self.data = {
            'action': 'user'
        }


    # Prueba cambiar rol a user exitosa
    def test_change_user_rol_successful(self):
        response = self.client.patch(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba cambiar rol a admin exitosa
    def test_change_admin_rol_successful(self):
        self.data['action'] = 'admin'
        response = self.client.patch(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba cambiar rol con parámetro incorrecto
    def test_change_user_role_invalid_action(self):
        self.data['action'] = 'invalid_action'
        response = self.client.patch(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba no existe usuario
    def test_change_status_user_not_found(self):
        url = reverse('change_user_role_admin', args=[12345])
        response = self.client.patch(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba sin autenticación
    def test_change_status_unauthenticated(self):
        self.client = APIClient()
        response = self.client.patch(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
