from django.db import models

class Accidente(models.Model):
    NumeroReferencia = models.IntegerField(primary_key=True)
    Fecha = models.DateField(null=True)
    Lugar = models.CharField(max_length=100, null=True)
    Hora = models.TimeField(null=True)


    def __str__(self):
      return f'{self.NumeroReferencia} {self.Fecha}'
    
