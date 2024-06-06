from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from datetime import datetime
from authentication.models import User, Rol


# Tests para el registro de usuarios
class SignUpTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('signUp')
        user_role = Rol.objects.create(rol='user')
        self.user_role_id = user_role.id
        self.data = {
            "full_name": "test fullname",
            "email": "test@email.com",
            "password": "testpassword",
            "phone": "+57 321 543 7665",
            "birth_date": "1999-09-09",
            "rol": self.user_role_id
        }

    # Prueba exitosa
    def test_successful(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba con datos faltantes
    def test_missing_data(self):
        del self.data['full_name']
        del self.data['email']
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba con email ya registrado
    def test_already_registered_email(self):
        User.objects.create(
            full_name="Existing User",
            email="test@email.com",
            password="existingpassword",
            phone="+57 321 543 7890",
            birth_date="1990-01-01",
            rol_id=self.user_role_id
        )
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba con email invalido
    def test_invalid_email(self):
        self.data['email'] = 'testemail.com'
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba con phone ya registrado
    def test_already_registered_phone(self):
        User.objects.create(
            full_name="Existing User",
            email="test1@email.com",
            password="existingpassword",
            phone="+57 321 543 7665",
            birth_date="1990-01-01",
            rol_id=self.user_role_id
        )
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba con birth_date invalido
    def test_invalid_birth_date(self):
        self.data['birth_date'] = datetime.now().strftime("%Y-%m-%d")
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba con rol invalido
    def test_invalid_rol(self):
        self.data['rol'] = 99
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)
