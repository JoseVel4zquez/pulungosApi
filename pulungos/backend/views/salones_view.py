from backend.models import salones


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from backend.serializers import salonesSerializer

# # Create your views here.
from django.contrib.auth.hashers import make_password
from rest_framework import status


@api_view(['GET'])
def getSalones(request):
    salon = salones.objects.all()
    serializer = salonesSerializer(salon, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createSalon(request):
    data = request.data
    try:
        salon = salones.objects.create(
            salon_nombre=data['salon_nombre'],

        )
        serializer = salonesSerializer(salon, many=False)
        return Response(serializer.data)
    except:
        message = {'error': 'alguno de los campos es invalido'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
