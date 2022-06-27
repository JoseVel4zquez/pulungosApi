from backend.models import roles


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from backend.serializers import RolesSerializer

# # Create your views here.
from django.contrib.auth.hashers import make_password
from rest_framework import status


@api_view(['GET'])
def getRoles(request):
    rol = roles.objects.all()
    serializer = RolesSerializer(rol, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createRol(request):
    data = request.data
    try:
        rol = roles.objects.create(
            nombre_rol=data['nombre_rol'],

        )
        serializer = RolesSerializer(rol, many=False)
        return Response(serializer.data)
    except:
        message = {'error': 'alguno de los campos es invalido'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
