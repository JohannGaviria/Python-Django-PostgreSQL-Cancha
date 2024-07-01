from django.urls import path
from . import views


# Rutas URLs para la app de gestion de reservas
urlpatterns = [
    path('reserve-court', views.reserve_court, name='reserve_court'),
    path('user-reservations', views.user_reservations, name='user_reservations'),
]