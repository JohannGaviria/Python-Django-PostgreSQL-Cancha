from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from django.utils import timezone
from django.db.models import Q
from authentication.models import User
from authentication.serializers import UserSerializer
from datetime import timedelta


# Lógica para actualizar al usuario
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_user(request):
    # Obtenemos al usuario autenticado 
    user = request.user

    # Serializamos los datos recibidos en la solicitud
    serializer = UserSerializer(user, data=request.data)

    # Verifica que los datos son validos 
    if serializer.is_valid():
        # Guarda el usuario
        serializer.save()

        # Obtiene el usuario recién actualizado
        user = User.objects.get(email=serializer.data['email'])
        # Hashea la contraseña del usuario
        user.set_password(request.data['password'])
        # Guarda el cambio
        user.save()

        # Elimina el token viejo del usuario
        Token.objects.filter(user=user).delete()

        # Crea un nuevo token para el usuario
        token = Token.objects.create(user=user)

        # Calcula la nueva fecha de expiración del token
        expiration = timezone.now() + timedelta(days=3)

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Successful update',
            'data': {
                'token': {
                    'token_key': token.key,
                    'token_expiration': expiration
                },
                'user': serializer.data
            }
        }, status=status.HTTP_200_OK)
    
    # Respuesta de error
    return Response({
        'status': 'errors',
        'message': 'Validation failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Lógica para eliminar al usuario
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_user(request):
    # Obtiene el usuario autenticado
    user = request.user

    # Elimina el usuario
    user.delete()

    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'successful deleted'
    }, status=status.HTTP_200_OK)


# Lógica para busqueda de usuarios por admin
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def search_users_admin(request):
    # Obtiene los parámetros de la URL
    query = request.query_params.get('query', None)

    # Si no se proporciona ningún parámetro de búsqueda, mostrar todos los usuarios
    if not query:
        # Obtiene todos los usuarios
        users = User.objects.all()
    else:
        # Busca usuarios que coincidan con el parámetro de búsqueda
        users = User.objects.filter(
            Q(full_name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query) |
            Q(rol__rol__icontains=query) |
            Q(is_active__icontains=query)
        ).distinct()

    # Serializa los datos de los usuarios
    serializer = UserSerializer(users, many=True)

    # Respuesta exitosa
    if not query:
        return Response({
            'status': 'success',
            'message': 'All users retrieved successfully',
            'data': {
                'result': len(serializer.data),
                'users': serializer.data
            }
        })
    else:
        return Response({
            'status': 'success',
            'message': 'User found successfully',
            'data': {
                'result': len(serializer.data),
                'users': serializer.data
            }
        })


# Lógica para activar/desactivar un usuario admin
@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def change_user_status_admin(request, user_id):
    # Buscar al usuario por el ID proporcionado
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'User not found'
        }, status=status.HTTP_404_NOT_FOUND)
    
    # Verifica si se está activando o desactivando al usuario
    action = request.data.get('action', None)

    if action == 'activate':
        # Activa al usuario
        user.is_active = True
        message = 'User activated successfully'
    elif action == 'deactivate':
        # Desactiva al usuario
        user.is_active = False
        message = 'User deactivated successfully'
    else:
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Invalid action provided'
        }, status=status.HTTP_400_BAD_REQUEST)

    # Guarda el cambio
    user.save()

    # Respuesta existosa
    return Response({
        'status': 'success',
        'message': message
    })
