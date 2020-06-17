from django.shortcuts import redirect
from django.views.generic import View, TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import AutorForm
from .models import Autor

# Create your views here.
class CrearAutor(CreateView):
    model = Autor
    template_name = 'autor/crear.html'
    form_class = AutorForm
    success_url = reverse_lazy('autor:listar')


class ListarAutor(ListView):
    template_name = 'autor/listar.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(eliminado=False)


class ActualizarAutor(UpdateView):
    model = Autor
    template_name = 'autor/crear.html'
    form_class = AutorForm
    success_url = reverse_lazy('autor:listar')


class EliminarAutor(DeleteView):
    model = Autor
    template_name = 'autor/eliminar.html'

    def post(self, request, pk, *args, **kwargs):
        object = Autor.objects.get(id=pk)
        object.eliminado = True
        object.save()
        return redirect('autor:listar')
