from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from .views import CrearLibro, ListarLibro, ActualizarLibro, EliminarLibro

urlpatterns = [
    path('crear/', login_required(CrearLibro.as_view()), name='crear'),
    path('listar/', login_required(ListarLibro.as_view()), name='listar'),
    path('editar/<int:pk>', login_required(ActualizarLibro.as_view()), name='editar'),
    path('eliminar/<int:pk>', login_required(EliminarLibro.as_view()), name='eliminar'),
]
