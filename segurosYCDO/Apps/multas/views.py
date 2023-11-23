from rest_framework import generics
from .models  import Multa
from .serializers import MultaSerializer

class MultaListCreateView(generics.ListCreateAPIView):
    queryset = Multa.objects.all()
    serializer_class = MultaSerializer
 