from django.db import models

class Multa(models.Model):
    NumeroReferencia = models.IntegerField(primary_key=True)
    Fecha = models.DateField(null=True)
    Hora = models.TimeField(null=True)
    LugarInfraccion = models.CharField(max_length=100, null=True)
    Importe = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
      return f'{self.NumeroReferencia}'
