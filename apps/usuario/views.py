from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Usuario
from .forms import LoginForm, UsuarioForm

# Create your views here.


class Inicio(TemplateView):
    template_name = 'index.html'

class CrearUsuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/crear.html'
    success_url = reverse_lazy('usuario:listar')

class ListarUsuario(ListView):
    model = Usuario
    template_name = 'usuario/listar.html'
    context_object_name = 'usuarios'
    
    def get_queryset(self):
        return self.model.objects.filter(activo=True)

class ActualizarUsuario(UpdateView):
    model = Usuario
    template_name = 'usuario/editar.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('usuario:listar')


class EliminarUsuario(DeleteView):
    model = Usuario
    template_name = 'usuario/eliminar.html'

    def post(self, request, pk, *args, **kwargs):
        object = self.model.objects.get(id=pk)
        object.activo = False
        object.save()
        return redirect('usuario:listar')

class Login(FormView):
    template_name = 'usuario/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/usuario/login')
