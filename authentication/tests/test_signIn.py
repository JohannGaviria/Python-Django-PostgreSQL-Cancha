from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from authentication.models import User, Rol


# Tests para el inicio de sesión de usuario
class SignInTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('signIn')
        user_role = Rol.objects.create(rol='user')
        self.user = User.objects.create_user(
            full_name="test fullname",
            email="test@email.com",
            password="testpassword",
            phone="+57 321 543 7665",
            birth_date="1999-09-09",
            rol=user_role
        )
        self.data = {
            "email": "test@email.com",
            "password": "testpassword"
        }


    # Prueba exitosa
    def test_successful(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba email incorrecto
    def test_incorrect_email(self):
        self.data['email'] = "incorrect@email.com"
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba password incorrecto
    def test_incorrect_password(self):
        self.data['password'] = "incorrectpassword"
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba usuario desactivado
    def test_deactivated_user(self):
        self.user.is_active = False
        self.user.save()
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)
