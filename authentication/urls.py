from django.urls import path
from . import views


# Rutas URLs para la app de aunteticación
urlpatterns = [
    path('signUp', views.signUp, name='signUp'),
    path('signIn', views.signIn, name='signIn'),
    path('signOut', views.signOut, name='signOut'),
]