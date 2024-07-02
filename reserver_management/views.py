from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from src.utils import get_paginated
from .models import StatusReservation, Reservation
from .serializers import ReservationSerializer


# Lógica para reservar una cancha
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def reserve_court(request):
    # Serializa los datos recibidos en la solicitud
    serializer = ReservationSerializer(data=request.data)

    # Verifica que los datos sean válidos
    if serializer.is_valid():
        # Obtiene los datos relevantes de la solicitud
        court = serializer.validated_data['court']
        start_datetime = serializer.validated_data['start_datetime']
        end_datetime = serializer.validated_data['end_datetime']

        # Obtiene una reservacion con los mismos datos
        overlapping_reservations = Reservation.objects.filter(
            court=court,
            start_datetime=start_datetime,
            end_datetime=end_datetime
        ).exists()

        # Verifica la disponibilidad de la cancha
        if overlapping_reservations:
            # Respuesta error
            return Response({
                'status': 'errors',
                'message': 'Validation failed',
                'errors': {
                    'court': [
                        'Court is already reserved for this time period'
                    ]
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Guarda la reserva si esta disponible
        serializer.save()

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Reservation created successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
    
    # Respuesta de error
    return Response({
        'status': 'errors',
        'message': 'Validation failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Lógiaca para que el usuario vea sus reservaciones
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_reservations(request):
    # Obtiene el usuario actual
    user = request.user

    # Obtiene todas las reservaciones del usuario
    reservations = Reservation.objects.filter(user=user).order_by('id')

    # Obtiene las paginas solicitadas
    pages = get_paginated(request, reservations, 10)

    # Serializa los datos
    serializer = ReservationSerializer(pages, many=True)

    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Reservations obtained correctly',
        'data': {
            'reservations': serializer.data
        }
    }, status=status.HTTP_200_OK)


# Lógica para cancelar una reservacion
@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cancel_reservation(request, reservation_id):
    try:
        # Intenta obtener la reservacion del ID
        reservation = Reservation.objects.get(id=reservation_id, user=request.user)
    except Reservation.DoesNotExist:
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': {
                'reservation': [
                    'Reservation not found'
                ]
            }
        }, status=status.HTTP_404_NOT_FOUND)
    
    # Actualiza el estado a cancelado
    reservation.status = StatusReservation.objects.get(status=StatusReservation.CANCELLED)
    
    # Guarda el cambio del estado
    reservation.save()
    
    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Reservation canceled correctly'
    }, status=status.HTTP_200_OK)


# Lógica para obtener todas las reservaciones por admin
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_reservations_admin(request):
    # Obtiene todas las reservaciones del usuario
    reservations = Reservation.objects.all().order_by('id')

    # Obtiene las paginas solicitadas
    pages = get_paginated(request, reservations, 10)

    # Serializa los datos
    serializer = ReservationSerializer(pages, many=True)

    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Reservations obtained correctly',
        'data': {
            'reservations': serializer.data
        }
    }, status=status.HTTP_200_OK)
