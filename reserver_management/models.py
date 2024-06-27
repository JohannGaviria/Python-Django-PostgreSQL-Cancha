from django.db import models
from authentication.models import User
from court_management.models import Court


# Definición del modelo de estado de reservacion
class StatusReservation(models.Model):
    status = models.CharField(max_length=100, null=False)


# Definición del modelo de reservacion
class Reservation(models.Model):
    start_datetime = models.DateTimeField(null=False)
    end_datetime = models.DateTimeField(null=False)
    status = models.ForeignKey(StatusReservation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
