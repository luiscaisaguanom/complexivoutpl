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
        return '{}:{}'.format(self.zona.codigo,self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Provincia, self).save()

    class Meta:
        verbose_name_plural = "Provincias"
        unique_together = ('codigo','nombre')

class Distrito(ClaseModelo):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    codigo = models.CharField(
        max_length=10,
        help_text='',
        unique=True
    )
    nombre = models.CharField(
        max_length=30,
        help_text='',
        unique=True
    )

    def __str__(self):
        return '{}:{}'.format(self.provincia.codigo,self.codigo)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Distrito, self).save()

    class Meta:
        verbose_name_plural = "Distritos"
        unique_together = ('codigo','nombre')

class Canton(ClaseModelo):
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    codigo = models.CharField(
        max_length=10,
        help_text='',
        unique=True
    )
    nombre = models.CharField(
        max_length=30,
        help_text='',
        unique=True
    )

    def __str__(self):
        return '{}:{}'.format(self.distrito.codigo,self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Canton, self).save()

    class Meta:
        verbose_name_plural = "Cantones"
        unique_together = ('codigo','nombre')

class Circuito(ClaseModelo):
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE)
    codigo = models.CharField(
        max_length=10,
        help_text='',
        unique=True
    )
    nombre = models.CharField(
        max_length=30,
        help_text='',
        unique=True
    )

    def __str__(self):
        return '{}:{}'.format(self.canton.codigo,self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Circuito, self).save()

    class Meta:
        verbose_name_plural = "Circuitos"
        unique_together = ('codigo','nombre')

class Subcircuito(ClaseModelo):
    circuito = models.ForeignKey(Circuito, on_delete=models.CASCADE)
    codigo = models.CharField(
        max_length=12,
        help_text='',
        unique=True
    )
    nombre = models.CharField(
        max_length=30,
        help_text='',
        unique=True
    )

    def __str__(self):
        return '{}:{}'.format(self.circuito.codigo,self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Subcircuito, self).save()

    class Meta:
        verbose_name_plural = "Subcircuitos"
        unique_together = ('codigo','nombre')