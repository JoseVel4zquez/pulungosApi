from os import name
from django.urls import path
from backend.views import salones_view as views

urlpatterns = [

    path('registrarSalon/', views.createSalon, name="regisro_rol"),
    path('lista/', views.getSalones, name='lista_roles'),
    # path('perfil/usuario/', views.UpdateUserProfile, name='perfil-usuario'),
    # path('perfil/<str:pk>/', views.getUserById, name='perfil-usuario'),
    # path('permisos/usuario/<str:pk>/',
    #      views.UpdateUserPermissions, name='user-permissions'),
    # path('eliminar/<str:pk>/', views.deleteUser, name="elimiar-usuario"),
    # path('imagenPerfil/<str:pk>/', views.uploadImageProfile, name='imagen-perfil'),
    # path('cv/<str:pk>/', views.uploadCv, name="CV-usuario")


]
