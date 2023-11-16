from rest_framework import serializers
from .models import Accidente

class AccidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accidente
        fields = '__all__'

