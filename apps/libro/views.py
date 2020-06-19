from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import LibroForm
from .models import Libro

# Create your views here.
class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/crear.html'
    success_url = reverse_lazy('libro:listar')

class ListarLibro(ListView):
    model = Libro
    template_name = 'libro/listar.html'
    context_object_name = 'libros'
    queryset = model.objects.filter(eliminado=False)

class ActualizarLibro(UpdateView):
    model = Libro
    template_name = 'libro/editar.html'
    form_class = LibroForm
    success_url = reverse_lazy('libro:listar')


class EliminarLibro(DeleteView):
    model = Libro
    template_name = 'libro/eliminar.html'

    def post(self, request, pk, *args, **kwargs):
        object = self.model.objects.get(id=pk)
        object.eliminado = True
        object.save()
        return redirect('libro:listar')