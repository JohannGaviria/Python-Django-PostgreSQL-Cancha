from django.contrib import admin
from django.urls import path, include


# Urls globales
urlpatterns = [
    path('admin/', admin.site.urls),

    # Urls para la API
    path('api/auth/', include('authentication.urls')),
    path('api/users/', include('users_management.urls')),
]
