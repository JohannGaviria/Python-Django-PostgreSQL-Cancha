from django.urls import path
from . import views


# Rutas URLs para la app de gestion de usuarios
urlpatterns = [
    path('update', views.update_user, name='update_user'),
    path('delete', views.delete_user, name='delete_user'),
]