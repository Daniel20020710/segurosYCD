from django.db import models

class Vehiculos(models.Model):
    matricula = models.CharField(max_length=45)
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)

    def __str__(self):
      return f'{self.matricula}'
