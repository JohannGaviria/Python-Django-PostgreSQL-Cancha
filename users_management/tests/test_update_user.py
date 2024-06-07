from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from datetime import datetime
from authentication.models import User, Rol


# Tests para actualizar usuario
class UpdateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('update_user')
        user_role = Rol.objects.create(rol='user')
        self.user = User.objects.create_user(
            full_name="test fullname",
            email="test@email.com",
            password="testpassword",
            phone="+57 321 543 7665",
            birth_date="1999-09-09",
            rol=user_role
        )
        self.user1 = User.objects.create_user(
            full_name="test fullname",
            email="testanother@email.com",
            password="testpassword",
            phone="+57 390 908 7656",
            birth_date="1999-09-09",
            rol=user_role
        )
        self.user_role_id = user_role.id
        self.data = {
            "full_name": "test new fullname",
            "email": "testnew@email.com",
            "password": "testnewpassword",
            "phone": "+57 321 543 7665",
            "birth_date": "1999-09-09",
            "rol": self.user_role_id
        }
        self.client.force_authenticate(user=self.user)


    # Prueba exitosa
    def test_successful(self):
        response = self.client.put(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)


    # Prueba con datos faltantes
    def test_missing_data(self):
        del self.data['full_name']
        del self.data['email']
        response = self.client.put(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba con email ya registrado
    def test_already_registered_email(self):
        self.data['email'] = 'testanother@email.com'
        response = self.client.put(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba con email invalido
    def test_invalid_email(self):
        self.data['email'] = 'testemail.com'
        response = self.client.put(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba con phone ya registrado
    def test_already_registered_phone(self):
        self.data['phone'] = '+57 390 908 7656'
        response = self.client.put(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba con birth_date invalido
    def test_invalid_birth_date(self):
        self.data['birth_date'] = datetime.now().strftime("%Y-%m-%d")
        response = self.client.put(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)


    # Prueba con rol invalido
    def test_invalid_rol(self):
        self.data['rol'] = 99
        response = self.client.put(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)
    

    # Prueba sin autenticación
    def test_without_authentication(self):
        client = APIClient()
        response = client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
