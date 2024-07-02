from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from court_management.models import Court
from src.utils import get_paginated
from .models import Review
from .serializers import ReviewSerializer


# Lógica para crear una review
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_review(request):
    # Serilaiza los datos recibidos en la solicitud
    serializer = ReviewSerializer(data=request.data)

    # Verifica que los datos son validos
    if serializer.is_valid():
        # Guarda los datos
        serializer.save()

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Review created successfully',
            'data': {
                'review': serializer.data
            }
        }, status=status.HTTP_201_CREATED)
    
    # Respuesta de error
    return Response({
        'status': 'errors',
        'message': 'Validation failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Lógica para ver las reviews de una cancha
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_review(request, court_id):
    try:
        # Busca la cancha correspodiente al ID
        Court.objects.get(id=court_id)
    except Court.DoesNotExist:
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': {
                'court': [
                    'Court not found'
                ]
            }
        }, status=status.HTTP_404_NOT_FOUND)

    # Obtiene las reviews correspodientes al ID
    reviews = Review.objects.filter(court=court_id).order_by('id')

    # Obtiene las paginas solicitadas
    pages = get_paginated(request, reviews, 10)

    # Serializa los datos
    serializer = ReviewSerializer(pages, many=True)

    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Review obtained correctly',
        'data': {
            'reviews': serializer.data
        }
    }, status=status.HTTP_200_OK)


# Lógica para ver todos los reviews por admin
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def list_all_reviews_admin(request):
    # Obtiene todas las reviews
    reviews = Review.objects.all().order_by('id')

    # Obtiene las paginas solicitadas
    pages = get_paginated(request, reviews, 10)

    # Serializa los datos
    serializer = ReviewSerializer(pages, many=True)

    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Reviews obtained correctly',
        'data': {
            'reviews': serializer.data
        }
    }, status=status.HTTP_200_OK)


# Lógica para eliminar una review por admin
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_review_admin(request, review_id):
    try:
        # Obtiene la review por su ID
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': {
                'review': [
                    'Review not found'
                ]
            }
        }, status=status.HTTP_404_NOT_FOUND)
    
    # Eliminar la review
    review.delete()

    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Review successfully deleted'
    }, status=status.HTTP_200_OK)
