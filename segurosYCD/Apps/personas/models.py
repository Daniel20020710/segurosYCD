from django.db import models

class TipoPersona(models.Model):
     estado_civil = models.CharField(max_length=45)

class Personas(models.Model):
    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    documento = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45, null=True)
    telefono = models.CharField(max_length=45, null=True)
    ciudad = models.CharField(max_length=45, null=True)
    tipo_persona = models.ForeignKey(TipoPersona, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
