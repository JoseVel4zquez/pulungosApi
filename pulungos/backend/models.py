from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.deletion import SET_NULL

# Create your models here.


class UserProfileManager(BaseUserManager):
    '''Manager  para perfiles de usuario'''

    def create_user(self, email, name, password=None):
        ''' crear nuevo user profile'''
        if not email:
            raise ValueError('Usuario debe tener un Email')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name,
                          id_rol=roles.objects.get(id_rol=2))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class roles(models.Model):
    id_rol = models.AutoField(primary_key=True, editable=False, null=False)
    nombre_rol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_rol


class salones(models.Model):
    id_trabajo = models.AutoField(primary_key=True, editable=False, null=False)
    salon_nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.trabajo_salonNombre


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """modelo baes de datos para usuarios en el sistema"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    edad = models.IntegerField(default=0)
    fecha_nacimiento = models.CharField(max_length=250)
    grabacion = models.FileField(null=True, blank=True)
    temperatura = models.CharField(max_length=250)
    id_trabajo = models.ForeignKey(
        salones, related_name="salon", on_delete=models.SET_NULL, null=True)
    id_rol = models.ForeignKey(
        roles, related_name="rol", on_delete=models.SET_NULL, null=True)

    image = models.ImageField(null=True, blank=True,
                              default="/placeholder.png")

    id = models.AutoField(primary_key=True, editable=False, null=False)
    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''obtener nombre completo del usuairo'''
        return self.name

    def get_short_name(self):
        '''obtener nombre corto del usuario'''
        return self.name

    def __str__(self):
        '''retornar cadena representando nuestro usuario'''
        return self.email


class padres(models.Model):
    id_padre = models.AutoField(primary_key=True, editable=False, null=False)
    nombre_padre = models.CharField(max_length=255)
    apellido_padre = models.CharField(max_length=250)
    fechaInscripcion = models.CharField(max_length=250)
    fechanacimiento = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    celular = models.IntegerField(default=0)
    telefonoCasa = models.IntegerField(default=0)
    telefonoOficina = models.IntegerField(default=0)
    huella = models.CharField(max_length=250)
    user_id = models.ForeignKey(
        UserProfile, related_name="rol", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre_padre


class preguntas(models.Model):
    id_trabajo = models.AutoField(primary_key=True, editable=False, null=False)
    pregunta_nombre = models.CharField(max_length=100)
    pregunta_respuesta = models.CharField(max_length=100)

    def __str__(self):
        return self.trabajo_nombre
