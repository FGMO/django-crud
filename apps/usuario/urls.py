from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from .views import Inicio, Login, logoutUsuario

urlpatterns = [
    path('', login_required(Inicio.as_view()), name='inicio'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', login_required(logoutUsuario), name='logout'),
]