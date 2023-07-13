from django.contrib import admin
from .models import *

# Register your models here.

class ConciertoAdmin(admin.ModelAdmin):
    list_display = ('idConcierto', 'artista')
    ordering = ['idConcierto']
    
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('idArtista', 'nomArtista', 'genero')
    ordering = ['nomArtista']
    
class RecintoAdmin(admin.ModelAdmin):
    list_display = ('idRecinto', 'nomRecinto', 'comuna')
    ordering = ['nomRecinto']
    
    
admin.site.register(Concierto, ConciertoAdmin)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Recinto, RecintoAdmin)
