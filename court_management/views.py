from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q
from src.utils import get_paginated
from .models import SurfaceType, CourtStatus, CourtType, Court, CourtImage
from .serializers import SurfaceTypeSerializer,  CourtStatusSerializer, CourtTypeSerializer, CourtSerializer, CourtImageSerializer


# Lógica para obtener y crear tipos de superficies por admin
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def surface_type_admin(request):
    # verifica que el metodo sea get para obtener los datos
    if request.method == 'GET':
        # Obtiene todos los datos del tipo de superficie
        surface_types = SurfaceType.objects.all().order_by('id')

        # Obtiene la páginas solicitada
        pages = get_paginated(request, surface_types, 10)

        # Serializa los datos obtenidos
        serializer = SurfaceTypeSerializer(pages, many=True)
        
        # Respuesta exitosa
        return Response({
            'status': 'success',
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
        court_status = CourtStatus.objects.all().order_by('id')

        # Obtiene la páginas solicitada
        pages = get_paginated(request, court_status, 10)

        # Serializa los datos obtenidos
        serializer = CourtStatusSerializer(pages, many=True)
        
        # Respuesta exitosa
        return Response({
            'status': 'success',
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
        court_types = CourtType.objects.all().order_by('id')

        # Obtiene la páginas solicitada
        pages = get_paginated(request, court_types, 10)

        # Serializa los datos obtenidos
        serializer = CourtTypeSerializer(pages, many=True)
        
        # Respuesta exitosa
        return Response({
            'status': 'success',
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
    # Serializa los datos recibidos en la solicitud
    serializer = CourtSerializer(data=request.data)

    # Verifica que los datos sean válidos
    if serializer.is_valid():
        # Guarda los datos
        serializer.save()

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Court created correctly',
            'data': {
                'court': serializer.data
            }
        }, status=status.HTTP_201_CREATED)
    
    # Respuesta de error
    return Response({
        'status': 'errors',
        'message': 'Validation failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Lógica para actualizar cancha por admin
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_court_admin(request, court_id):
    try:
        # Obtiene la cancha por ID
        court = Court.objects.get(id=court_id)
    except Court.DoesNotExist:
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': {
                'court_id': [
                    'The specified court does not exist.'
                ]
            }
        }, status=status.HTTP_404_NOT_FOUND)

    # Serializa la cancha con los datos proporcionados en la solicitud
    serializer = CourtSerializer(court, data=request.data)

    # Verifica que los datos son válidos
    if serializer.is_valid():
        # Actualiza la cancha
        serializer.save()

        # Respesta exitosa
        return Response({
            'status': 'success',
            'message': 'Court updated correctly',
            'data': {
                'court': serializer.data
            }
        }, status=status.HTTP_200_OK)

    # Respuesta de error
    return Response({
        'status': 'errors',
        'message': 'Validation failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Lógica para eliminar cancha por admin
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_court_admin(request, court_id):
    try:
        # Obtiene la cancha por ID
        court = Court.objects.get(id=court_id)
    except Court.DoesNotExist:
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': {
                'court_id': [
                    'The specified court does not exist.'
                ]
            }
        }, status=status.HTTP_404_NOT_FOUND)
    
    # Elimina la cancha
    court.delete()

    # Respesta ecitosa
    return Response({
        'status': 'success',
        'message': 'Court deleted successfully'
    }, status=status.HTTP_200_OK)


# Lógica para agregar imagenes de las canchas por admin
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def add_court_image_admin(request):
    # Serializa los datos recibidos en la solicitud
    serializer = CourtImageSerializer(data=request.data)

    # Verifica que los datos son válidos
    if serializer.is_valid():
        # Guarda la imagen
        serializer.save()

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Court image added successfully',
            'data': {
                'image_court': serializer.data
            }
        }, status=status.HTTP_201_CREATED)
    
    # Respuesta de error
    return Response({
        'status': 'errors',
        'message': 'Validation failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Lógica para obtener las imagenes de la cancha por admin
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_court_image_admin(request, court_id):
    try:
        # Obtiene la cancha por ID
        Court.objects.get(id=court_id)
    except Court.DoesNotExist:
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': {
                'court_id': [
                    'The specified court does not exist.'
                ]
            }
        }, status=status.HTTP_404_NOT_FOUND)

    # Obtiene todas las imagenes de la cancha
    court_image = CourtImage.objects.filter(court=court_id)
    
    # Serializa los datos
    serializer = CourtImageSerializer(court_image, many=True)

    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Court images geted successfully',
        'data': serializer.data
    }, status=status.HTTP_200_OK)


# Lógica para eliminar las imagenes de la cancha por admin
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_court_image_admin(request, image_id):
    try:
        # Obtiene la cancha por ID
        court_image = CourtImage.objects.get(id=image_id)
    except CourtImage.DoesNotExist:
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': {
                'court_image_id': [
                    'The specified court image does not exist.'
                ]
            }
        }, status=status.HTTP_404_NOT_FOUND)
    
    # Elimina la imagen de la cancha
    court_image.delete()

    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Court images deleted successfully'
    }, status=status.HTTP_200_OK)


# Lógica para buscar canchas
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def search_courts(request):
    # Obtiene los parámetros de la URL
    query = request.query_params.get('query', None)

    if not query:
        # Obtiene todas las canchas si no hay query
        courts = Court.objects.all()
    else:
        # Filtra las canchas que coincidan con el parámetro de búsqueda
        courts = Court.objects.filter(
            Q(name__icontains=query) |
            Q(code__icontains=query) |
            Q(size__icontains=query) |
            Q(location__icontains=query) |
            Q(price_hour__icontains=query) |
            Q(description__icontains=query) |
            Q(surface_type__type=query) |
            Q(court_status__status=query) |
            Q(court_type__type=query)
        ).distinct()

    # Serializa los datos de las canchas
    court_serializer = CourtSerializer(courts, many=True)

    # Obtener los IDs de las canchas filtradas
    court_ids = courts.values_list('id', flat=True)

    # Filtrar las imágenes de las canchas correspondientes
    court_images = CourtImage.objects.filter(court_id__in=court_ids)

    # Serializar las imágenes de las canchas
    image_serializer = CourtImageSerializer(court_images, many=True)

    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Curts correctly obtained',
        'data': {
            'result': len(court_serializer.data),
            'courts': court_serializer.data,
            'court_images': image_serializer.data
        }
    }, status=status.HTTP_200_OK)
