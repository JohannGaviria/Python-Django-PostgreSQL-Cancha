from django.urls import path
from . import views


# Rutas URLs para la app de review
urlpatterns = [
    path('create-review', views.create_review, name='create_review'),
    path('list-review/<int:court_id>', views.list_review, name='list_review'),
    path('list-all', views.list_all_reviews_admin, name='list_all_reviews_admin'),
    path('delete-review/<int:review_id>', views.delete_review_admin, name='delete_review_admin'),
]