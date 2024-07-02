from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from src.utils import get_paginated
from .models import Review
from .serializers import ReviewSerializer


# Lógica para crear una review
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_review(request):
    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Review created successfully',
        'data': {

        }
    }, status=status.HTTP_201_CREATED)


# Lógica para ver las reviews de una cancha
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_review(request, court_id):
    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Review obtained correctly',
        'data': {

        }
    }, status=status.HTTP_200_OK)


# Lógica para ver todos los reviews por admin
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def list_all_reviews_admin(request):
    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Reviews obtained correctly',
        'data': {

        }
    }, status=status.HTTP_200_OK)


# Lógica para eliminar una review por admin
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_review_admin(request, review_id):
    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Review successfully deleted'
    }, status=status.HTTP_200_OK)
