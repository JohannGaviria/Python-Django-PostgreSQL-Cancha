from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.test import TestCase
from authentication.models import User, Rol
from court_management.models import SurfaceType, CourtStatus, CourtType, Court
from reserver_management.models import StatusReservation


# Tests para la creacion de reservas    
class GetReservationsAdminTests(TestCase):    
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('get_reservations_admin')
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
        self.status_reservation = StatusReservation.objects.create(status=StatusReservation.AVAILABLE)
        self.reservation = {
            'start_datetime': '2024-07-01T14:30',
            'end_datetime': '2024-07-01T16:30',
            'status': self.status_reservation,
            'user': self.user,
            'court': self.court,
        }

    # Prueba exitosa
    def test_successfully(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('data' in response.data)
