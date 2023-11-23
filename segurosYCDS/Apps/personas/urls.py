from django.urls import path
from .views import TipoPersonaListCreateView, PersonaListCreateView

urlpatterns = [
   
    path('', PersonaListCreateView.as_view(), name='personas'),
     path('', TipoPersonaListCreateView.as_view(), name='tipoPersonas'),
]
