from django.urls import path
from . import views


# Rutas URLs para la app de gestion de usuarios
urlpatterns = [
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),
]