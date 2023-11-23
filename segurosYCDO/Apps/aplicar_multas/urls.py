from django.urls import path
from .views import AplicarMultasListCreateView
urlpatterns = [
    path('', AplicarMultasListCreateView.as_view(), name='aplicarMultas'),
]
 