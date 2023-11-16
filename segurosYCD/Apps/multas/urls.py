from django.urls import path
from .views import MultaListCreateView
urlpatterns = [
    path('', MultaListCreateView.as_view(), name='multas'),
]
 