from django.contrib.auth.models import User
from backend.models import UserProfile, salones, roles


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from backend.serializers import UserSerializer, UserSerializerWithToken

# # Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registrarNino(request):
    data = request.data
    usuario = UserProfile.objects.create(
        email=data['correo'],
        name=data['nombre'],
        lastname=data['apellido'],
        edad=data['edad'],
        temperatura=data['temperatura'],
        fecha_nacimiento=data['fecha_nacimiento'],
        id_trabajo=salones.objects.get(id_trabajo=data['id_salon']),
        id_rol=roles.objects.get(id_rol=1),
        image=request.FILES.get('image'),
        grabacion=request.FILES.get('grabacion'),
        password=make_password(data['password']),

    )
    serializer = UserSerializerWithToken(usuario, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getMyUsers(request):
    usuarios = UserProfile.objects.all()
    serializer = UserSerializer(usuarios, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserprofile(request):
    usuario = request.user
    serializer = UserSerializer(usuario, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request, pk):
    usuario = UserProfile.objects.get(id=pk)
    usuario.delete()
    return Response('usuario eliminado con exito')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserById(request, pk):
    user = UserProfile.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UpdateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)
    data = request.data
    user.email = data['correo']
    user.name = data['nombre']
    user.lastname = data['apellido']
    user.edad = data['edad']
    user.temperatura = data['temperatura']
    user.id_trabajo = data['id_trabajo']

    if data['password'] != '':
        user.password = data['password']
    user.save()
    return Response(serializer.data)
