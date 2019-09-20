from django import forms
from .models import Autor


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = [
            'apellidos',
            'nombres',
            'descripcion',
        ]
        labels = {
            'apellidos': 'Apellidos del Autor',
            'nombres': 'Nombres del Autor',
            'descripcion': 'Descripción'
        }
        widgets = {
            'apellidos': forms.TextInput(
                attrs={
                    'id': 'nombres',
                    'class': 'form-control',
                    'placeholder': 'Ingrese los nombres del autor'
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'id': 'apellidos',
                    'class': 'form-control',
                    'placeholder': 'Ingrese los apellidos del autor'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'id': 'descripcion',
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción para el autor'}
            )
        }
