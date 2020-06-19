from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from .views import Inicio, Login, logoutUsuario, CrearUsuario, ListarUsuario, ActualizarUsuario, EliminarUsuario

urlpatterns = [
    path('', login_required(Inicio.as_view()), name='inicio'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', login_required(logoutUsuario), name='logout'),
    path('crear/', login_required(CrearUsuario.as_view()), name='crear'),
    path('listar/', login_required(ListarUsuario.as_view()), name='listar'),
    path('editar/<int:pk>', login_required(ActualizarUsuario.as_view()), name='editar'),
    path('eliminar/<int:pk>', login_required(EliminarUsuario.as_view()), name='eliminar'),
]