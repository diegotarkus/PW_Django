from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('conciertos/', conciertos, name='conciertos'),
    path('conciertos/recinto/<recinto>', conciertos_recinto, name='conciertos-recinto'),
    path('contact/', contacto, name='contact'),
    path('api/', api, name='api'),
    path('about/', about, name='about'),
    path('infomacion/<str:concierto_id>', informacion, name='informacion'),
    path('registrar/', registrar, name='registrar'),
    path('login/', login, name='login'),
    path('logout', logout, name='logout'),
]