from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import User
from .serializers import UserSerializer


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


# Logica para inicio de sesión de usuario
@api_view(['POST'])
def signIn(request):
    # Devuelve los datos
    return Response({
        'status': 'succes',
        'message': 'Successful login',
        'data': {
            'user': []
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
