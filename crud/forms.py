from django import forms
from django.forms import ModelForm
from .models import *

class ConciertoList(ModelForm):
    class Meta:
        model = Concierto
        fields = [
            'idConcierto',
            'artista',          
            'recinto',
            'fecha',
            'valores',
            'venta',
            'imagen'           
        ]
        
        labels = {
            'idConcierto' : 'IdConcierto',            
            'artista' : 'Artista',            
            'recinto' : 'Recinto',
            'fecha' : 'Fecha',
            'valores' : 'Entradas desde',
            'venta' : 'Link de compra',
            'imagen' : 'Imagen'
        }
        
        widgets = {
            'idConcierto' : forms.TextInput(attrs={'class':'form-control'}),
            'artista' : forms.Select(attrs={'class':'form-control'}),
            'recinto' : forms.Select(attrs={'class':'form-control'}),
            'fecha' : forms.TextInput(attrs={'class':'form-control'}),
            'valores' : forms.TextInput(attrs={'class':'form-control'}),
            'venta' : forms.TextInput(attrs={'class':'form-control'}),
            'imagen' : forms.FileInput(attrs={'class':'form-control'})
        }

class RecintoList(ModelForm):
    class Meta:
        model = Recinto
        fields = [
            'idRecinto',
            'nomRecinto',
            'capacidad',
            'comuna',
            'direccion',
            'estacionamiento'        
        ]
        
        labels = {
            'idRecinto' : 'ID Recinto',
            'nomRecinto' : 'Nombre Recinto',
            'capacidad' : 'Capacidad',
            'comuna' : 'Comuna',
            'direccion' : 'Dirección',
            'estacionamiento' : 'Estacionamiento'            
        }
        
        widgets = {
            'idRecinto' : forms.TextInput(attrs={'class':'form-control'}),
            'nomRecinto' : forms.TextInput(attrs={'class':'form-control'}),
            'capacidad' : forms.TextInput(attrs={'class':'form-control', 'type' : 'number'}),
            'comuna' : forms.TextInput(attrs={'class':'form-control'}),
            'direccion' : forms.TextInput(attrs={'class':'form-control'}),
            'estacionamiento' : forms.TextInput(attrs={'class':'form-control'}),
        }
        
class ArtistaList(ModelForm):
    class Meta:
        model = Artista
        fields = [
            'idArtista',
            'nomArtista',
            'pais',
            'genero',
            'anio',
            'playlist'
        ]
            
        labels = {
            'idArtista' : 'ID Artista',
            'nomArtista' : 'Nombre artista',
            'pais' : 'Lugar de origen',
            'genero' : 'Género',
            'anio' : 'Año de debut',
            'playlist' : 'Playlist'
        }
            
        widgets = {
            'idArtista' : forms.TextInput(attrs={'class':'form-control'}),
            'nomArtista' : forms.TextInput(attrs={'class':'form-control'}),
            'pais' : forms.TextInput(attrs={'class':'form-control'}),
            'genero' : forms.TextInput(attrs={'class':'form-control'}),
            'anio' : forms.TextInput(attrs={'class':'form-control', 'type' : 'number'}),
            'playlist' : forms.TextInput(attrs={'class':'form-control'})
        }
        