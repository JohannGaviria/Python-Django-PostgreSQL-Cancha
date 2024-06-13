from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from src.utils import get_paginated
from .models import SurfaceType, CourtStatus, CourtType, Court, CourtImage
from .serializers import SurfaceTypeSerializer,  CourtStatusSerializer, CourtTypeSerializer, CourtSerializer


# Lógica para obtener y crear tipos de superficies por admin
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def surface_type_admin(request):
    # verifica que el metodo sea get para obtener los datos
    if request.method == 'GET':
        # Obtiene todos los datos del tipo de superficie
        surface_types = SurfaceType.objects.all()

        # Obtiene la páginas solicitada
        pages = get_paginated(request, surface_types, 10)

        # Serializa los datos obtenidos
        serializer = SurfaceTypeSerializer(pages, many=True)
        
        # Respuesta exitosa
        return Response({
            'staus': 'success',
            'message': 'Correctly obtained surface types',
            'data': {
                'surface_type': serializer.data
            }
        })
    
    # Verifica que el metodo sea post para crear nuevos datos
    if request.method == 'POST':
        # Serializa los datos recibidos en la solicitud
        serializer = SurfaceTypeSerializer(data=request.data)

        # Verifica si los datos son válidos
        if serializer.is_valid():
            # Guarda los datos
            serializer.save()

            # Respuesta exitosa
            return Response({
                'status': 'success',
                'message': 'Successfully created surface type',
                'data': {
                    'surface_type': serializer.data
                }
            }, status=status.HTTP_201_CREATED)
        
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# Lógica para obtener y crear estado de canchas por admin
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def court_status_admin(request):
    # verifica que el metodo sea get para obtener los datos
    if request.method == 'GET':
        # Obtiene todos los datos del estado de la cancha
        court_status = CourtStatus.objects.all()

        # Obtiene la páginas solicitada
        pages = get_paginated(request, court_status, 10)

        # Serializa los datos obtenidos
        serializer = SurfaceTypeSerializer(pages, many=True)
        
        # Respuesta exitosa
        return Response({
            'staus': 'success',
            'message': 'Correctly obtained court status',
            'data': {
                'court_status': serializer.data
            }
        })
    
    # Verifica que el metodo sea post para crear nuevos datos
    if request.method == 'POST':
        # Serializa los datos recibidos en la solicitud
        serializer = CourtStatusSerializer(data=request.data)

        # Verifica si los datos son válidos
        if serializer.is_valid():
            # Guarda los datos
            serializer.save()

            # Respuesta exitosa
            return Response({
                'status': 'success',
                'message': 'Successfully created court status',
                'data': {
                    'court_status': serializer.data
                }
            }, status=status.HTTP_201_CREATED)
        
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# Lógica para obtener y crear tipos de canchas por admin
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def court_type_admin(request):
    # verifica que el metodo sea get para obtener los datos
    if request.method == 'GET':
        # Obtiene todos los datos del tipo de cancha
        court_types = CourtType.objects.all()

        # Obtiene la páginas solicitada
        pages = get_paginated(request, court_types, 10)

        # Serializa los datos obtenidos
        serializer = CourtTypeSerializer(pages, many=True)
        
        # Respuesta exitosa
        return Response({
            'staus': 'success',
            'message': 'Correctly obtained court types',
            'data': {
                'court_type': serializer.data
            }
        })
    
    # Verifica que el metodo sea post para crear nuevos datos
    if request.method == 'POST':
        # Serializa los datos recibidos en la solicitud
        serializer = CourtTypeSerializer(data=request.data)

        # Verifica si los datos son válidos
        if serializer.is_valid():
            # Guarda los datos
            serializer.save()

            # Respuesta exitosa
            return Response({
                'status': 'success',
                'message': 'Successfully created court type',
                'data': {
                    'court_type': serializer.data
                }
            }, status=status.HTTP_201_CREATED)
        
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# Lógica para agregar nueva cancha por admin
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def add_court_admin(request):
    # Respesta exitosa
    return Response({
        'status': 'success',
        'message': 'Court created correctly',
        'data': {
            'court'
        }
    }, status=status.HTTP_201_CREATED)


# Lógica para actualizar cancha por admin
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_court_admin(request):
    # Respesta ecitosa
    return Response({
        'status': 'success',
        'message': 'Court updated correctly',
        'data': {
            'court'
        }
    }, status=status.HTTP_200_OK)


# Lógica para eliminar cancha por admin
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_court_admin(request):
    # Respesta ecitosa
    return Response({
        'status': 'success',
        'message': 'Court deleted successfully',
        'data': {
            'court'
        }
    }, status=status.HTTP_200_OK)
