from django.urls import path
from . import views


# Rutas URLs para la app de gestion de reservas
urlpatterns = [
    path('reserve-court', views.reserve_court, name='reserve_court'),
    path('user-reservations', views.user_reservations, name='user_reservations'),
    path('reservations', views.get_reservations_admin, name='get_reservations_admin'),
    path('cancel-reservation/<int:reservation_id>', views.cancel_reservation, name='cancel_reservation'),
]