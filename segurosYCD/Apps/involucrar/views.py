from rest_framework import generics
from .models  import Involucrar
from .serializers import InvolucrarSerializer

class InvolucrarListCreateView(generics.ListCreateAPIView):
    queryset = Involucrar.objects.all()
    serializer_class = InvolucrarSerializer
 