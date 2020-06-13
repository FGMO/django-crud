from django.db import models

# Create your models here.


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    apellidos = models.CharField(
        'Apellidos', max_length=200, blank=False, null=False)
    nombres = models.CharField(
        'Nombres', max_length=100, blank=False, null=False)
    descripcion = models.TextField('Descripción', blank=True, null=True)
    adicionado = models.DateField('Adicionado', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    eliminado = models.BooleanField('Eliminado', default=False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['id']

    def __str__(self):
        return '{nombres} {apellidos}'.format(apellidos=self.apellidos, nombres=self.nombres)
