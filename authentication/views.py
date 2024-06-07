from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import User
from .serializers import UserSerializer
from datetime import timedelta


# Lógica para registro de usuario
@api_view(['POST'])
def signUp(request):
    # Serializa los datos recibidos en la solicitud
    serializer = UserSerializer(data=request.data)

    # Verifica que los datos son válidos
    if serializer.is_valid():
        # Guarda el usuario
        serializer.save()

        # Obtiene el usuario recién registrado
        user = User.objects.get(email=serializer.data['email'])
        # Hashea la contraseña del usuario
        user.set_password(request.data['password'])
        # Guarda el cambio
        user.save()
        
        # Crea un token de autenticación para el usuario
        token = Token.objects.create(user=user)

        # Respuesta de exito con los datos
        return Response({
            'status': 'success',
            'message': 'Successful registration',
            'data': {
                'token' : {
                    'token_key': token.key
                },
                'user': serializer.data
            }
        }, status=status.HTTP_201_CREATED)

    # Respuesta de error
    return Response({
        'status': 'errors',
        'message': 'Validation failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Lógica para inicio de sesión de usuario
@api_view(['POST'])
def signIn(request):
    # Obtiene los datos recibidos en la solicitud
    email = request.data.get('email')
    password = request.data.get('password')

    # Buscar el usuario por su email
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # Respuesta de error
        return Response({
        'status': 'errors',
        'message': 'Validation failed',
        'errors': {
            'email': [
                'Email is incorrect'
            ]
        }
    }, status=status.HTTP_400_BAD_REQUEST)

    # Verifica la contraseña
    if not user.check_password(password):
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': {
                'password': [
                    'Password is incorrect'
                ]
            }
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Verifica que el usuario este activo
    if not user.is_active:
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': {
                'user': [
                    'User not active'
                ]
            }
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Calcula la fecha de expiración del token
    expiration = timezone.now() + timedelta(days=3)

    # Crea el token del usuario
    token, _ = Token.objects.get_or_create(user=user)

    # Serializa los datos del usuario
    serializer = UserSerializer(user)

    # Respuesta de exito con los datos
    return Response({
        'status': 'succes',
        'message': 'Successful login',
        'data': {
            'token': {
                'token_key': token.key,
                'token_expiration': expiration
            },
            'user': serializer.data
        }
    }, status=status.HTTP_200_OK)


# Logica para el cierre de sesión de usuario
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def signOut(request):
    # Devuelve los datos
    return Response({
        'status': 'succes',
        'message': 'Successful logout',
    }, status=status.HTTP_200_OK)
