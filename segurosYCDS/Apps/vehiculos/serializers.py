from rest_framework import serializers
from .models import Vehiculos

class VehiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculos
        fields = '__all__'

 