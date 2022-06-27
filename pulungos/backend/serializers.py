from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserProfile, roles, salones, padres, preguntas


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    id = serializers.SerializerMethodField(read_only=True)
    is_staff = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id',  'email', 'name', 'lastname', 'edad', 'password', 'is_staff', 'image', 'temperatura',
                  "id_rol", "fecha_nacimiento", "id_trabajo", "grabacion"]

    def get_id(self, obj):
        return obj.id

    def get_is_staff(self, obj):
        return obj.is_staff

    def get_id_rol(self, obj):
        return obj.id_rol

    def get_name(self, obj):
        name = obj.name
        if name == '':
            name = obj.email
        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id',  'email', 'name', 'lastname', 'edad', 'is_staff', 'image', 'temperatura',
                  "id_rol", "fecha_nacimiento", "id_trabajo", 'password', "grabacion", 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = roles
        fields = '__all__'


class salonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = salones
        fields = '__all__'


class padresSerializer(serializers.ModelSerializer):
    class Meta:
        model = padres
        fields = '__all__'


class preguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = preguntas
        fields = '__all__'
