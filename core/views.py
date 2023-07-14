from django.shortcuts import render, HttpResponse, redirect, reverse
from crud.models import Concierto, Recinto, Artista
from django.contrib import messages
from .models import *
import bcrypt
from .forms import *


# Create your views here.

def root(request):
    return redirect('/home')

def home(request):
    context = {'conciertos': Concierto.objects.all()}
    return render(request,'core/home.html',context)

def conciertos(request):
    context = {'conciertos': Concierto.objects.all()}
    return render(request,'core/conciertos.html',context)

def conciertos_recinto(request, recinto):
    context = {'conciertos': Concierto.objects.filter(recinto = recinto),'recintos': Recinto.objects.all()}
    return render(request,'core/conciertos.html',context)

def informacion(request, concierto_id):
    concierto = Concierto.objects.get(idConcierto=concierto_id)
    if concierto:
        context = {'concierto':concierto}
        return render(request,'core/informacion.html',context)

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST, request.FILES)
        if form.is_valid():
            id = form.cleaned_data.get('id')
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            correo = form.cleaned_data.get('correo')
            telefono = form.cleaned_data.get('telefono')
            mensaje = form.cleaned_data.get('mensaje')
            obj = DatosContacto.objects.create(
                id = id,
                nombre = nombre,
                apellido = apellido,
                correo = correo,
                telefono = telefono,
                mensaje = mensaje
            )
            obj.save()
            return redirect(reverse('contact')+ '?OK')
        else:
            return redirect(reverse('contact')+ '?FAIL')
    else:
        form = ContactoForm
    return render(request,'core/contact.html',{'form':form})

def api(request):
    return render(request, 'core/api.html')

def about(request):
    return render(request, 'core/about.html')

def registrar(request):
    if request.method == 'POST':
        errors = Usuario.objects.validador(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
                request.session['registro_nombre'] = request.POST['nombre']
                request.session['registro_apellido'] = request.POST['apellido']
                request.session['registro_email'] = request.POST['correo']
                request.session['level_mensaje'] = 'alert-danger'

        else:
            request.session['registro_nombre'] = ""
            request.session['registro_apellido'] = ""
            request.session['registro_email'] = ""

            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            correo = request.POST['correo']
            password = request.POST['password']
            password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

            obj = Usuario.objects.create(
                nombre=nombre, 
                apellido=apellido,
                correo=correo,
                password_decode=password,
                password=password_hash
            )
            obj.save()
            messages.success(request, "Usuario registrado.")
            request.session['level_mensaje'] = 'alert-success'
        
            return redirect(reverse('conciertos')+ '?OK')
            
    return render(request,'core/registrar.html')

def login(request):
    if request.method == 'POST':
        usuario = Usuario.objects.filter(correo=request.POST['email_login'])
        
        if usuario:
            user_regis = usuario[0]
            
            if bcrypt.checkpw(request.POST['password_login'].encode(), user_regis.password.encode()): 
                usuario = {
                    'id':user_regis.id,
                    'nombre':user_regis.nombre,
                    'apellido':user_regis.apellido,
                    'correo':user_regis.correo,
                    'rol':user_regis.rol,
                }

                request.session['usuario'] = usuario
                messages.success(request,"Usuario ingresado.")
                
                return redirect(reverse('conciertos')+ '?OK_USER')
            else:
                messages.error(request,"Contraseña incorrecta.")
                return render(request,'/')
        else:
            messages.error(request,"Datos incorrectos.")
            return render(request,'/')
    return render(request,'core/login.html')

def logout(request):
    if 'usuario' in request.session:
        del request.session['usuario']
    
    return redirect('/')
