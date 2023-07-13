from rest_framework import serializers
from crud.models import *

class ConciertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concierto
        fields = (
            'idConcierto','artista','fecha','recinto','valores','venta'
        )

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = (
            'id','artista', 'pais', 'genero'
        )