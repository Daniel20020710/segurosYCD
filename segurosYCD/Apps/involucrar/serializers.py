from rest_framework import serializers
from .models import Involucrar

class InvolucrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Involucrar
        fields = '__all__'

 