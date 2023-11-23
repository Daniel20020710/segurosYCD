from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status
from .models import TipoPersona, Personas
from .serializers import TipoPersonaSerializer, PersonaSerializer

class TipoPersonaListCreateView(generics.ListCreateAPIView):
    queryset = TipoPersona.objects.all()
    serializer_class = TipoPersonaSerializer

class PersonaListCreateView(generics.ListCreateAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonaSerializer
