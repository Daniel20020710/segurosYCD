from django.urls import path
from .views import PropietariosListCreateView
urlpatterns = [
    path('', PropietariosListCreateView.as_view(), name='propietarios'),
]
 