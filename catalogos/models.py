from django.db import models
from bases.models import ClaseModelo

# Create your models here.
class Rango(ClaseModelo):
    nombre = models.CharField(
        max_length=15,
        help_text='Rango del Personal',
        unique=True
    )
    
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Rango, self).save()

    class Meta:
        verbose_name_plural = "Rangos"

class Tipo_Vehiculo(ClaseModelo):
    nombre = models.CharField(
        max_length=15,
        help_text='Tipo de Vehículo',
        unique=True
    )
    
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Tipo_Vehiculo, self).save()

    class Meta:
        verbose_name_plural = "Tipos_Vehiculos"

class Tipo_Mantenimiento(ClaseModelo):
    nombre = models.CharField(
        max_length=20,
        help_text='Tipo de Mantenimiento',
        unique=True
    )
    
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Tipo_Mantenimiento, self).save()

    class Meta:
        verbose_name_plural = "Tipos_Mantenimientos"
