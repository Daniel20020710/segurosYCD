from django.urls import path
from .views import InvolucrarListCreateView
urlpatterns = [
    path('', InvolucrarListCreateView.as_view(), name='involucrar'),
]
 