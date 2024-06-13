from django.urls import path
from . import views


# Rutas URLs para la app de gestion de canchas
urlpatterns = [
    path('surface-types', views.surface_type_admin, name='surface_type_admin'),
    path('court-status', views.court_status_admin, name='court_status_admin'),
    path('court-types', views.court_type_admin, name='court_type_admin'),
    path('add-court', views.add_court_admin, name='add_court_admin'),
    path('update-court/<int:court_id>', views.update_court_admin, name='update_court_admin'),
    path('delete-court/<int:court_id>', views.delete_court_admin, name='delete_court_admin'),
]