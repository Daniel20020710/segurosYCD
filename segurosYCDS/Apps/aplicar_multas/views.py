from rest_framework import generics
from .models  import AplicarMultas
from .serializers import AplicarMultasSerializer

class AplicarMultasListCreateView(generics.ListCreateAPIView):
    queryset = AplicarMultas.objects.all()
    serializer_class = AplicarMultasSerializer
