from django.db import models
from Apps.personas.models import Personas
from Apps.vehiculos.models import Vehiculos

class Propietarios(models.Model):
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)

    def __str__(self):
      return f'{self.persona} {self.vehiculo}'