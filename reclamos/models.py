from django.db import models
from dependencias.models import Circuito, Subcircuito

# Create your models here.
class Reclamos(models.Model):
    circuito = models.ForeignKey(Circuito, on_delete=models.CASCADE)
    subcircuito = models.ForeignKey(Subcircuito, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10)
    detalles = models.CharField(max_length=200)
    contacto = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fc = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.detalle)
    
    def save(self):
        self.detalles = self.detalles.upper()
        super(Reclamos, self).save()

    class Meta:
        verbose_name_plural = "Reclamos"
