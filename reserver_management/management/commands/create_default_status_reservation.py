from django.core.management.base import BaseCommand
from reserver_management.models import StatusReservation

"""
Crea los estatus de las reservas:

python manage.py create_default_status_reservation
"""

class Command(BaseCommand):
    help = 'Create default status reservation'

    def handle(self, *args, **kwargs):
        # Verificar si ya existen los estados de reservacion
        if not StatusReservation.objects.exists():
            # Crear instancias de StatusReservation para 'Available', 'Confirmed' y 'Cancelled'
            StatusReservation.objects.create(status=StatusReservation.AVAILABLE)
            StatusReservation.objects.create(status=StatusReservation.CONFIRMED)
            StatusReservation.objects.create(status=StatusReservation.CANCELLED)
            self.stdout.write(self.style.SUCCESS('Successfully created status reservation'))
        else:
            self.stdout.write(self.style.WARNING('Status reservation already exist'))