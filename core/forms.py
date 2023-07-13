from django import forms
from django.forms import ModelForm
from .models import *

class ContactoForm(ModelForm):
    class Meta:
        model = DatosContacto
        fields = [
            'id',
            'nombre',
            'apellido',
            'correo',
            'telefono',
            'mensaje'
        ]
        
        labels = {
            'id' : 'ID',
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'correo' : 'Correo',
            'telefono' : 'Telefono',
            'mensaje' : 'Mensaje'
        }
        
        widgets = {
            'id' : forms.TextInput(attrs={'class':'form-control'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'apellido' : forms.TextInput(attrs={'class':'form-control'}),
            'correo' : forms.TextInput(attrs={'class':'form-control'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control', 'type' : 'number'}),
            'mensaje' : forms.TextInput(attrs={'class':'form-control', 'id' : 'mensaje'}),
        }