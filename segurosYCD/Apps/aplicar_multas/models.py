from django.db import models
from Apps.multas.models import Multa
from Apps.personas.models import Personas
from Apps.vehiculos.models import Vehiculos

class AplicarMultas(models.Model):
    multa = models.ForeignKey(Multa, on_delete=models.CASCADE)
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
    def __str__(self):
      return f'{self.multa}'
