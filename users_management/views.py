from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.utils import timezone
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
