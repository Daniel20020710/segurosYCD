from django.urls import path
from .views import AccidenteListCreateView
urlpatterns = [
    path('', AccidenteListCreateView.as_view(), name='accidente'),
]
