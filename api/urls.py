from django.urls import path
from .views import *

urlpatterns = [
    path('conciertos/', lista_concert),
]