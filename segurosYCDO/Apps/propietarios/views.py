from rest_framework import generics
from .models  import Propietarios
from .serializers import PropietariosSerializer

class PropietariosListCreateView(generics.ListCreateAPIView):
    queryset = Propietarios.objects.all()
    serializer_class = PropietariosSerializer
 