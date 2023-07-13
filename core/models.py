from django.db import models
import re

# Create your models here.


## CONTACTO

class DatosContacto(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    nombre = models.CharField(verbose_name='Nombre', max_length=30)
    apellido = models.CharField(verbose_name='Apellido', max_length=30)
    correo = models.EmailField(verbose_name='Correo', max_length=250)
    telefono = models.IntegerField(verbose_name='Teléfono')
    mensaje = models.CharField(verbose_name='Mensaje',max_length=100)
    
    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'
        ordering = ['id']
        
    def __str__(self) -> str:
        return self.nombre   
    
## REGISTRO DE USUARIO    
class UserManager(models.Manager):
    def validador(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z.]+$')
        PASSWORD_REGEX = re.compile(r'^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$')
    
        errors = {}
    
        if len(Usuario.objects.filter(correo=postData['correo'])) > 0:
           errors['correo_exits'] = "Correo ya existente."
    
        else:
            if len(postData['nombre'].strip()) < 2 or len(postData['nombre'].strip()) > 40:
                errors['nombre_len'] = "Nombre debe tener entre 2 y 40 caracteres"
            if len(postData['apellido'].strip()) < 2 or len(postData['apellido'].strip()) > 40:
                 errors['apellido_len'] = "Apellido debe tener entre 2 y 40 caracteres"
            
        if not SOLO_LETRAS.match(postData['nombre']) or not SOLO_LETRAS.match(postData['apellido']):
            errors['solo_letras']  = "Favor ingresar solo letras."
        
        if not EMAIL_REGEX.match(postData['correo']):
            errors['correo'] = "Correo no válido."
            
        if not PASSWORD_REGEX.match(postData['password']):
            errors['password_format'] = "Formato de contraseña no válido"
            
        if postData['password'] != postData['password_confirm']:
            errors['password_confirm'] = "Contraseñas no coinciden"

        return errors
    
class Usuario(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=40)
    apellido = models.CharField(verbose_name='Apellido', max_length=40)
    correo = models.CharField(verbose_name='Correo', max_length=30, unique=True)
    password = models.CharField(verbose_name='Password', max_length=500)
    rol = models.CharField(verbose_name='Rol', max_length=20, default='USER')
    creado = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    actualizado = models.DateField(verbose_name='Actualizado', auto_now=True)    
    objects = UserManager()
    
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["correo"]

    def __str__(self) -> str:
        return self.nombre + " " + self.apellido
    
