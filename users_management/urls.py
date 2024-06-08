from django.urls import path
from . import views


# Rutas URLs para la app de gestion de usuarios
urlpatterns = [
    path('update', views.update_user, name='update_user'),
    path('delete', views.delete_user, name='delete_user'),
    path('search', views.search_users_admin, name='search_users_admin'),
    path('change-status/<int:user_id>', views.change_user_status_admin, name='change_user_status_admin'),
]