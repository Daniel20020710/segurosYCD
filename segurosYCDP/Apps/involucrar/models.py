from django.db import models
from Apps.accidentes.models import Accidente
from Apps.personas.models import Personas
from Apps.vehiculos.models import Vehiculos

class Involucrar(models.Model):
    accidente = models.ForeignKey(Accidente, on_delete=models.CASCADE)
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
    
    def __str__(self):
      return f'{self.accidente}'
