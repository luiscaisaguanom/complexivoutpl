from django.db import models
from bases.models import ClaseModelo

# Create your models here.
class Zona(ClaseModelo):
    codigo = models.CharField(
        max_length=10,
        help_text='Código de la Zona',
        unique=True
    )
    nombre = models.CharField(
        max_length=30,
        help_text='Nombre de la Zona',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.codigo)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Zona, self).save()

    class Meta:
        verbose_name_plural = "Zonas"


class Provincia(ClaseModelo):
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    codigo = models.CharField(
        max_length=10,
        help_text='Código de la Provincia',
        unique=True
    )
    nombre = models.CharField(
        max_length=30,
        help_text='Nombre de la Provincia',
        unique=True
    )

    def __str__(self):
        return '{}:{}'.format(self.zona.codigo,self.codigo)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Provincia, self).save()

    class Meta:
        verbose_name_plural = "Provincias"
        unique_together = ('codigo','nombre')