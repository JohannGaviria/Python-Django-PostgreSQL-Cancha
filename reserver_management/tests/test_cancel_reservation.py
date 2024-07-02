from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from authentication.models import User, Rol
from court_management.models import SurfaceType, CourtStatus, CourtType, Court
from reserver_management.models import StatusReservation, Reservation
import datetime


# Tests para cancelar reservaciones
class CancelReservationTests(TestCase):    
    def setUp(self):
        self.client = APIClient()
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
        StatusReservation.objects.create(status=StatusReservation.CANCELLED)
        self.reservation = Reservation.objects.create(
            start_datetime=timezone.make_aware(datetime.datetime(2024, 7, 1, 14, 30)),
            end_datetime=timezone.make_aware(datetime.datetime(2024, 7, 1, 16, 30)),
            status=self.status_reservation,
            user=self.user,
            court=self.court,
        )
        self.url = reverse('cancel_reservation', args=[self.reservation.id])

    
    # Prueba exitosa
    def test_successfully(self):
        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)


    # Prueba no existe la reservacion
    def test_does_not_exist(self):
        self.url = reverse('cancel_reservation', args=[999])
        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue('status' in response.data)
        self.assertTrue('message' in response.data)
        self.assertTrue('errors' in response.data)
