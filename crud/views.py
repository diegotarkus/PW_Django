from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import *
from .forms import *
# Create your views here.

def root(request):
    return redirect('conciertos/')

## CONCIERTOS

def lista_concert(request):
    context = {'conciertos': Concierto.objects.all()}
    return render(request,'crud/conciertos.html',context)

def concierto_nuevo(request):
    if request.method == 'POST':
        form = ConciertoList(request.POST, request.FILES)
        if form.is_valid():
            idConcierto = form.cleaned_data.get('idConcierto')
            fecha = form.cleaned_data.get('fecha')
            valores = form.cleaned_data.get('valores')
            imagen = form.cleaned_data.get('imagen')
            venta = form.cleaned_data.get('venta')
            artista = form.cleaned_data.get('artista')
            recinto = form.cleaned_data.get('recinto')
            obj = Concierto.objects.create(
                idConcierto = idConcierto,
                fecha = fecha,
                valores = valores,
                imagen = imagen,
                venta = venta,
                artista = artista,
                recinto = recinto,                
            )
            obj.save()
            return redirect (reverse('crud-conciertos') + '?OK')
        else:
            return redirect (reverse('crud-conciertos') + '?FAIL')
    else:
        form = ConciertoList
    return render (request, 'crud/conciertos-nuevo.html', {'form' : form})


def concierto_editar(request,concierto_id):
    try:
        concierto = Concierto.objects.get(idConcierto = concierto_id)
        form = ConciertoList(instance=concierto)

        if request.method == 'POST':
            form = ConciertoList(request.POST, request.FILES, instance=concierto)
            if form.is_valid():
                form.save()
                return redirect(reverse('crud-conciertos') + '?UPDATED')
            else:
                return redirect(reverse('conciertos-editar') + concierto_id) 

        context = {'form':form}
        return render(request,'crud/conciertos-editar.html',context)
    except:
        return redirect(reverse('crud-conciertos') + '?NO_EXISTS')
    
    
def concierto_borrar(request,concierto_id):
    try:
        concierto = Concierto.objects.get(idConcierto = concierto_id)
        concierto.delete()
        return redirect(reverse('crud-conciertos') + '?DELETED')
    except:
        return redirect(reverse('crud-conciertos') + '?FAIL')
    
def concierto_info(request, concierto_id):
    try:
        concierto = Concierto.objects.get(idConcierto=concierto_id)
        if concierto:
            context = {'concierto':concierto}
            return render(request,'crud/conciertos-info.html',context)
        else:
            return redirect(reverse('crud-conciertos') + '?OK')
    except:
        return redirect(reverse('crud-conciertos') + '?FAIL')
    
def conciertos_por_recinto(request, recinto):
    try:
        recintos = Concierto.objects.filter(recinto=recinto)
        if recintos:
            context = {'recintos':recintos}
            return render(request,'crud/conciertos.html',context)
        else:
            return redirect(reverse('conciertos') + '?FAIL')
    except:
        return redirect(reverse('conciertos') + '?FAIL')
    
## ARTISTAS

def lista_artistas(request):
    context = {'artistas': Artista.objects.all()}
    return render(request,'crud/artistas.html',context)  

def artista_nuevo(request):
    if request.method == 'POST':
        form = ArtistaList(request.POST, request.FILES)
        if form.is_valid():
            idArtista = form.cleaned_data.get('idArtista')
            nomArtista = form.cleaned_data.get('nomArtista')
            pais = form.cleaned_data.get('pais')
            anio = form.cleaned_data.get('anio')
            genero = form.cleaned_data.get('genero')
            playlist = form.cleaned_data.get('playlist')
            obj = Artista.objects.create(
                idArtista = idArtista,
                nomArtista = nomArtista,
                pais = pais,
                anio = anio,
                genero = genero,
                playlist = playlist            
            )
            obj.save()
            return redirect (reverse('artistas') + '?OK')
        else:
            return redirect (reverse('artistas') + '?FAIL')
    else:
        form = ArtistaList
    return render (request, 'crud/artistas-nuevo.html', {'form' : form})  

def artista_editar(request,artista_id):
    try:
        artista = Artista.objects.get(idArtista = artista_id)
        form = ArtistaList(instance=artista)

        if request.method == 'POST':
            form = ArtistaList(request.POST, request.FILES, instance=artista)
            if form.is_valid():
                form.save()
                return redirect(reverse('artistas') + '?UPDATED')
            else:
                return redirect(reverse('artistas-editar') + artista_id) 

        context = {'form':form}
        return render(request,'crud/artistas-editar.html',context)
    except:
        return redirect(reverse('artista') + '?NO_EXISTS')
    
    
def artista_borrar(request,artista_id):
    try:
        artista = Artista.objects.get(idArtista = artista_id)
        artista.delete()
        return redirect(reverse('artistas') + '?DELETED')
    except:
        return redirect(reverse('artistas') + '?FAIL')
    
def artista_info(request, artista_id):
    try:
        artista = Artista.objects.get(idArtista=artista_id)
        if artista:
            context = {'artista':artista}
            return render(request,'crud/artistas-info.html',context)
        else:
            return redirect(reverse('artistas') + '?OK')
    except:
        return redirect(reverse('artistas') + '?FAIL')
            
## RECINTOS

def lista_recintos(request):
    context = {'recinto': Recinto.objects.all()}
    return render(request,'crud/recintos.html',context)

def recinto_nuevo(request):
    if request.method == 'POST':
        form = RecintoList(request.POST, request.FILES)
        if form.is_valid():
            idRecinto = form.cleaned_data.get('idRecinto')
            nomRecinto = form.cleaned_data.get('nomRecinto')
            capacidad = form.cleaned_data.get('capacidad')
            comuna = form.cleaned_data.get('comuna')
            direccion = form.cleaned_data.get('direccion')
            estacionamiento = form.cleaned_data.get('estacionamiento')
            obj = Recinto.objects.create(
                idRecinto = idRecinto,
                nomRecinto = nomRecinto,
                capacidad = capacidad,
                comuna = comuna,
                direccion = direccion,
                estacionamiento = estacionamiento         
            )
            obj.save()
            return redirect (reverse('recintos') + '?OK')
        else:
            return redirect (reverse('recintos') + '?FAIL')
    else:
        form = RecintoList
    return render (request, 'crud/recintos-nuevo.html', {'form' : form})  

def recinto_editar(request,recinto_id):
    try:
        recinto = Recinto.objects.get(idRecinto = recinto_id)
        form = RecintoList(instance=recinto)

        if request.method == 'POST':
            form = RecintoList(request.POST, request.FILES, instance=recinto)
            if form.is_valid():
                form.save()
                return redirect(reverse('recintos') + '?UPDATED')
            else:
                return redirect(reverse('recintos-editar') + recinto_id) 

        context = {'form':form}
        return render(request,'crud/recintos-editar.html',context)
    except:
        return redirect(reverse('recinto') + '?NO_EXISTS')
    
    
def recinto_borrar(request,recinto_id):
    try:
        recinto = Recinto.objects.get(idRecinto = recinto_id)
        recinto.delete()
        return redirect(reverse('recintos') + '?DELETED')
    except:
        return redirect(reverse('recintos') + '?FAIL')
    
def recinto_info(request, recinto_id):
    try:
        recinto = Recinto.objects.get(idRecinto=recinto_id)
        if recinto:
            context = {'recinto':recinto}
            return render(request,'crud/recintos-info.html',context)
        else:
            return redirect(reverse('recintos') + '?OK')
    except:
        return redirect(reverse('recintos') + '?FAIL')

              