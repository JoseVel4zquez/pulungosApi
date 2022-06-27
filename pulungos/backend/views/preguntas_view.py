from backend.models import preguntas


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from backend.serializers import preguntasSerializer

# # Create your views here.
from django.contrib.auth.hashers import make_password
from rest_framework import status


@api_view(['GET'])
def getPreguntas(request):
    pregunta = preguntas.objects.all()
    serializer = preguntasSerializer(pregunta, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createPregunta(request):
    data = request.data
    try:
        pregunta = preguntas.objects.create(
            pregunta_nombre=data['pregunta_nombre'],
            pregunta_respuesta=data['pregunta_respuesta'],

        )
        serializer = preguntasSerializer(pregunta, many=False)
        return Response(serializer.data)
    except:
        message = {'error': 'alguno de los campos es invalido'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
