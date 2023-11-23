from rest_framework import serializers
from .models import TipoPersona, Personas

class TipoPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPersona
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    tipo_persona = TipoPersonaSerializer()

    class Meta:
        model = Personas
        fields = '__all__'

    def create(self, validated_data):
        # Extraer los datos para el tipo_persona
        tipo_persona_data = validated_data.pop('tipo_persona')
        
        # Crear la instancia de TipoPersona
        tipo_persona = TipoPersona.objects.create(**tipo_persona_data)

        # Asignar la instancia de TipoPersona a la Persona
        persona = Personas.objects.create(tipo_persona=tipo_persona, **validated_data)

        return persona
