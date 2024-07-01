from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Reservation
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
