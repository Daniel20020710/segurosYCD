from rest_framework import serializers
from .models import Propietarios

class PropietariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propietarios
        fields = '__all__'

 