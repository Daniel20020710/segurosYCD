from rest_framework import generics
from .models  import Accidente
from .serializers import AccidenteSerializer

class AccidenteListCreateView(generics.ListCreateAPIView):
    queryset = Accidente.objects.all()
    serializer_class = AccidenteSerializer
