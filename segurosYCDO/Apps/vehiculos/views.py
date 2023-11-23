from rest_framework import generics
from .models  import Vehiculos
from .serializers import VehiculosSerializer

class VehiculosListCreateView(generics.ListCreateAPIView):
    queryset = Vehiculos.objects.all()
    serializer_class = VehiculosSerializer
 