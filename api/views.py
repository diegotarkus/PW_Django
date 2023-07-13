from django.shortcuts import render, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.http.response import JsonResponse

from crud.models import *
from .serializers import *

# Create your views here.
@api_view(['GET','POST','DELETE'])
def lista_concert(request):
    if request.method == 'GET':
        conciertos = Concierto.objects.all()

        artista = request.query_params.get('artista',None)
        if artista is not None:
            conciertos = conciertos.filter(artista__contains=artista)

        fecha = request.query_params.get('fecha',None)
        if fecha is not None:
            conciertos = conciertos.filter(fecha__contains=fecha)

        recinto = request.query_params.get('recinto',None)
        if recinto is not None:
            conciertos = conciertos.filter(recinto__recinto__contains=recinto)

        conciertos_serializer = ConciertoSerializer(conciertos,many=True)
        return Response(conciertos_serializer.data)
    
    elif request.method == 'POST':
        concierto_data = JSONParser().parse(request)
        concierto_serializer = ConciertoSerializer(data=concierto_data)
        if concierto_serializer.is_valid():
            concierto_serializer.save()
            return JsonResponse(concierto_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(concierto_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cantidad = Concierto.objects.all().delete()
        return Response({'mensaje':'Se han eliminado {} conciertos.'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','PUT','DELETE'])
def concierto_detail(request, concierto_id):
    try:
        concierto = Concierto.objects.get(idConcierto=concierto_id)
    except:
        return Response({'mensaje':'Concierto {} no existe en nuestros registros.'.format(concierto_id)},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        concierto_serializer = ConciertoSerializer(concierto)
        return Response(concierto_serializer.data)
    
    elif request.method == 'PUT':
        concierto_data = JSONParser().parse(request)
        concierto_serializer = ConciertoSerializer(concierto,data=concierto_data)
        if concierto_serializer.is_valid():
            concierto_serializer.save()
            return JsonResponse(concierto_serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(concierto_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        concierto.delete()
        return Response({'mensaje':'El concierto {} ha sido eliminado'.format(concierto_id)},status=status.HTTP_204_NO_CONTENT)