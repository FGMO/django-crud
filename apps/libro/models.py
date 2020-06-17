from django.db import models
from ..autor.models import Autor

# Create your models here.


class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    autor_id = models.ManyToManyField(Autor)
    fecha_publicacion = models.DateField(blank=False, null=False)
    # autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)
    adicionado = models.DateField('Adicionado', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    eliminado = models.BooleanField('Eliminado', default=False)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return '{titulo}'.format(titulo=self.titulo)
