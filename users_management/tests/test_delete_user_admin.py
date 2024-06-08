from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from authentication.models import User, Rol


# Tests para eliminar usuario
class DeleteUserAdminTestCase(TestCase):
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
        self.url = reverse('delete_user_admin', args=[self.user.id])


    # Prueba exitosa
    def test_successful(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
    

    # Prueba eliminar a un admin
    def test_delete_admin(self):
        user = User.objects.create_superuser(
            full_name="test Admin",
            email="admin1@example.com",
            password="adminpassword",
            phone="+57 311 203 4354",
            birth_date="1990-01-01"
        )
        url = reverse('delete_user_admin', args=[user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba sin autenticación
    def test_without_authentication(self):
        client = APIClient()
        response = client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
