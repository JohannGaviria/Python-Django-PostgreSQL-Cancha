from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    # Método para crear un usuario regular
    def create_user(self, email, password=None, rol=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        if rol is None:
            raise ValueError('Rol is required')
        email = self.normalize_email(email)
        user = self.model(email=email, rol=rol, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    # Método para crear un superusuario
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('The superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('The superuser must have is_superuser=True.')

        rol, created = Rol.objects.get_or_create(rol=Rol.ADMIN)
        return self.create_user(email, password, rol=rol, **extra_fields)


# Definición del modelo de Roles
class Rol(models.Model):
    ADMIN = 'admin'
    USER = 'user'
    USER_TYPE = [
        (ADMIN, 'Admin'),
        (USER, 'User'),
    ]

    rol = models.CharField(max_length=50, choices=USER_TYPE, default=USER, null=False)


    def __str__(self):
        return self.rol


# Definición del modelo de usuarios
class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=50, null=False, unique=True)
    birth_date = models.DateField(null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone', 'birth_date']

    objects = CustomUserManager()

    @property
    def is_admin(self):
        return self.rol.rol == Rol.ADMIN


    @property
    def is_user(self):
        return self.rol.rol == Rol.USER
