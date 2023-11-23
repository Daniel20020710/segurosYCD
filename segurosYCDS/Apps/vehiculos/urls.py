from django.urls import path
from .views import VehiculosListCreateView
urlpatterns = [
    path('', VehiculosListCreateView.as_view(), name='vehiculos'),
]
 