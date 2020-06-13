from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model=Libro
        fields=(
            'titulo',
            'autor_id',
            'fecha_publicacion',
        )
        labels={
            'titulo' : 'Título',
            'autor_id':'Autor(es)',
            'fecha_publicacion':'Fecha de publicación',
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'id': 'titulo',
                    'class': 'form-control',
                    'placeholder': 'Ingrese el título del libro'
                }
            ),
            'autor_id': forms.SelectMultiple(
                attrs={
                    'id': 'autor',
                    'class': 'form-control',
                    # 'placeholder': 'Ingrese el/los autor(es) del libro'
                }
            ),
            'fecha_publicacion': forms.SelectDateWidget(
                attrs={
                    'id': 'fecha_publicacion',
                    # 'class': 'form-control col-md-2',
                    'placeholder': 'Ingrese la fecha de publicación del libro'}
            )
        }