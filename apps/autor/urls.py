from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from .views import CrearAutor,  ListarAutor, ActualizarAutor, EliminarAutor

urlpatterns = [
    path('crear/', login_required(CrearAutor.as_view()), name='crear'),
    path('listar/', login_required(ListarAutor.as_view()), name='listar'),
    path('editar/<int:pk>', login_required(ActualizarAutor.as_view()), name='editar'),
    path('eliminar/<int:pk>', login_required(EliminarAutor.as_view()), name='eliminar'),
]