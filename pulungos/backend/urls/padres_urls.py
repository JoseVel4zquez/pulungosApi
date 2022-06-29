from os import name
from django.urls import path
from backend.views import padres_view as views

urlpatterns = [

    path('registrarPadres/', views.registrarPadre, name="regisro_rol"),
    path('lista/', views.getMyUsers, name='lista_roles'),
    # path('perfil/usuario/', views.UpdateUserProfile, name='perfil-usuario'),
    path('padre/<str:pk>/', views.getUserById, name='perfil-usuario'),
    # path('permisos/usuario/<str:pk>/',
    #      views.UpdateUserPermissions, name='user-permissions'),
    path('actualizarHuella/<str:pk>/',
         views.UpdateTouchId, name="actualizar-huella"),
    # path('imagenPerfil/<str:pk>/', views.uploadImageProfile, name='imagen-perfil'),
    # path('cv/<str:pk>/', views.uploadCv, name="CV-usuario")


]
