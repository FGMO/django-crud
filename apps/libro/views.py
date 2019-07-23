from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor

# Create your views here.


def Home(request):
    return render(request, 'index.html')


def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('libro:listar_autor')
    else:
        autor_form = AutorForm()
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form})


def editarAutor(request, id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id=id)
        if request.method == 'GET':
            autor_form = AutorForm(instance=autor)
        else:
            autor_form = AutorForm(request.POST, instance=autor)
            if autor_form.is_valid:
                autor_form.save()
                return redirect('libro:listar_autor')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form, 'error': error})

# def eliminarAutor(request, id):
#     autor = Autor.objects.get(id=id)
#     autor.delete()
#     return redirect('libro:listar_autor')

def eliminarAutor(request, id):
    autor = Autor.objects.get(id=id)
    if request.method == 'POST':
        # autor.delete()
        autor.eliminado = True
        autor.save()
        return redirect('libro:listar_autor')
    return render(request, 'libro/eliminar_autor.html', {'autor': autor})

def listarAutor(request):
    # autores = Autor.objects.all()
    autores = Autor.objects.filter(eliminado = False)
    return render(request, 'libro/listar_autor.html', {'autores': autores})
