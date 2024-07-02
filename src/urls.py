from django.contrib import admin
from django.urls import path, include


# Urls globales
urlpatterns = [
    path('admin/', admin.site.urls),

    # Urls para la API
    path('api/auth/', include('authentication.urls')),
    path('api/users/', include('users_management.urls')),
    path('api/courts/', include('court_management.urls')),
    path('api/reserves/', include('reserver_management.urls')),
    path('api/reviews/', include('review.urls'))
]
