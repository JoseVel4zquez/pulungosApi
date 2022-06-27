from os import name
from django.urls import path
from backend.views import user_view as views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('registrar/', views.registrarNino, name="regisro"),
    path('lista/', views.getMyUsers, name='lista_usuarios'),
    path('perfil/usuario/', views.UpdateUserProfile, name='perfil-usuario'),
    path('perfil/<str:pk>/', views.getUserById, name='perfil-usuario'),
    # path('permisos/usuario/<str:pk>/',
    #      views.UpdateUserPermissions, name='user-permissions'),
    path('eliminar/<str:pk>/', views.deleteUser, name="elimiar-usuario"),
    # path('imagenPerfil/<str:pk>/', views.uploadImageProfile, name='imagen-perfil'),
    # path('cv/<str:pk>/', views.uploadCv, name="CV-usuario")


]
