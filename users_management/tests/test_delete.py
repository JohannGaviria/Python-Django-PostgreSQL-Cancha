from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from authentication.models import User, Rol


# Tests para eliminar usuario
class DeleteTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('delete')
        user_role = Rol.objects.create(rol='user')
        self.user = User.objects.create_user(
            full_name="test fullname",
            email="test@email.com",
            password="testpassword",
            phone="+57 321 543 7665",
            birth_date="1999-09-09",
            rol=user_role
        )
        self.client.force_authenticate(user=self.user)


    # Prueba exitosa
    def test_successful(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
    

    # Prueba sin autenticación
    def test_without_authentication(self):
        client = APIClient()
        response = client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
