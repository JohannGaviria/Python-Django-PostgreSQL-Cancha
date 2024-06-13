from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from authentication.models import User, Rol


# Tests para búsqueda de usuarios
class SearchUsersAdminTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('search_users_admin')
        user_role = Rol.objects.create(rol='user')
        User.objects.create_user(
            full_name="test fullname",
            email="test@email.com",
            password="testpassword",
            phone="+57 321 543 7665",
            birth_date="1999-09-09",
            rol=user_role
        )
        self.admin_user = User.objects.create_superuser(
            full_name="test Admin",
            email="admin@example.com",
            password="adminpassword",
            phone="+57 301 203 4354",
            birth_date="1990-01-01"
        )
        self.client.force_authenticate(user=self.admin_user)


    # Prueba con parametro exitosa
    def test_with_parameter_successful(self):
        url = self.url + f'?query=Usuario'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba sin parametro exitosa
    def test_withoul_parameter_successful(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba sin autenticación
    def test_without_authentication(self):
        self.client = APIClient()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
