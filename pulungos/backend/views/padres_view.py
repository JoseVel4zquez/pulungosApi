from django.contrib.auth.models import User
from backend.models import UserProfile, padres

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from backend.serializers import padresSerializer

from rest_framework import status


@api_view(['POST'])
@permission_classes([IsAdminUser])
def registrarPadre(request):
    data = request.data
    padre = padres.objects.create(
        nombre_padre=data['nombre_padre'],
        apellido_padre=data['apellido_padre'],
        fechaInscripcion=data['fechaInscripcion'],
        fechanacimiento=data['fechanacimiento'],
        direccion=data['direccion'],
        celular=data['celular'],
        telefonoCasa=data['telefonoCasa'],
        telefonoOficina=data['telefonoOficina'],
        huella=data['huella'],
        user_id=UserProfile.objects.get(id=data['id_user'])
    )
    serializer = padresSerializer(padre, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserById(request, pk):
    padre = padres.objects.get(id_padre=pk)
    serializer = padresSerializer(padre, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getMyUsers(request):
    padre = padres.objects.all()
    serializer = padresSerializer(padre, many=True)
    return Response(serializer.data)
