from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('conciertos/', lista_concert, name='crud-conciertos'),
    path('conciertos/nuevo', concierto_nuevo, name='conciertos-nuevo'),
    path('conciertos/editar/<str:concierto_id>', concierto_editar, name='conciertos-editar'),
    path('conciertos/<str:concierto_id>/borrar', concierto_borrar, name='conciertos-borrar'),
    path('conciertos/info/<str:concierto_id>', concierto_info, name='conciertos-info'),
    path('conciertos/recintos/<recinto>', conciertos_por_recinto, name="concierto-recinto"),
    path('artistas/', lista_artistas, name='artistas'),
    path('artistas/nuevo', artista_nuevo, name='artistas-nuevo'),
    path('artistas/editar/<str:artista_id>', artista_editar, name='artistas-editar'),
    path('artistas/<str:artista_id>/borrar', artista_borrar, name='artistas-borrar'),
    path('artistas/info/<str:artista_id>', artista_info, name='artistas-info'),
    path('recintos/', lista_recintos, name='recintos'),
    path('recintos/nuevo', recinto_nuevo, name='recintos-nuevo'),
    path('recintos/editar/<str:recinto_id>', recinto_editar, name='recintos-editar'),
    path('recintos/<str:recinto_id>/borrar', recinto_borrar, name='recintos-borrar'),
    path('recintos/info/<str:recinto_id>', recinto_info, name='recintos-info'),    
]