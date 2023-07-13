from django.db import models
from datetime import datetime

# Create your models here.

class Artista(models.Model):
    idArtista = models.AutoField(primary_key=True, verbose_name='idArtista')
    nomArtista = models.CharField(verbose_name='Artista', max_length=50)
    pais = models.CharField(verbose_name='País', max_length=50)
    anio = models.CharField(verbose_name='Año de formación', max_length=4)
    genero = models.CharField(verbose_name='Género', max_length=70, null=True)
    playlist = models.URLField(verbose_name='Playlist', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        ordering = ['nomArtista', 'genero']

    def __str__(self) -> str:
        return self.nomArtista
    
class Recinto(models.Model):
    idRecinto = models.AutoField(primary_key=True, verbose_name='idRecinto')
    nomRecinto = models.CharField(verbose_name='Recinto', max_length=80)
    capacidad = models.IntegerField(verbose_name='Capacidad')
    comuna = models.CharField(verbose_name='Comuna', max_length=50)
    direccion = models.CharField(verbose_name='Dirección', max_length=250)
    estacionamiento = models.CharField(verbose_name='Estacionamiento', max_length=3)
    
    def __str__(self) -> str:
        return self.nomRecinto
    
class Concierto(models.Model):
    idConcierto = models.AutoField(primary_key=True, verbose_name='idConcierto')
    artista = models.ForeignKey(Artista, verbose_name='Artista', on_delete=models.CASCADE)
    recinto = models.ForeignKey(Recinto, verbose_name='Recinto', on_delete=models.CASCADE)
    fecha = models.DateTimeField(verbose_name='Fecha', max_length=60)
    valores = models.CharField(verbose_name='Entradas desde', max_length=500)
    venta = models.URLField(verbose_name='Link de venta', max_length=500, null=True, blank=True)
    imagen = models.ImageField(verbose_name='Imagen', upload_to='concierto', null=True, blank=True)
    
    class Meta:
        verbose_name = 'concierto'
        verbose_name_plural = 'conciertos'
        ordering = ['fecha','idConcierto']

    def __str__(self) -> str:
        return self.idConcierto
    
   

