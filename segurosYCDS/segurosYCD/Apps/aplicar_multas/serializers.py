from rest_framework import serializers
from .models import AplicarMultas

class AplicarMultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AplicarMultas
        fields = '__all__'

