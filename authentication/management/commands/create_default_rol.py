from django.core.management.base import BaseCommand
from authentication.models import Rol

"""
Crea los roles de usuarios:

python manage.py create_default_rol
"""

class Command(BaseCommand):
    help = 'Create default user roles'

    def handle(self, *args, **kwargs):
        # Verificar si ya existen los roles de usuario
        if not Rol.objects.exists():
            # Crear instancias de Rol para 'admin' y 'user
            Rol.objects.create(rol=Rol.ADMIN)
            Rol.objects.create(rol=Rol.USER)
            self.stdout.write(self.style.SUCCESS('Successfully created user roles'))
        else:
            self.stdout.write(self.style.WARNING('User roles already exist'))