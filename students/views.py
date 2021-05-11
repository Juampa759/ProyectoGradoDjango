from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.http import HttpResponse
from students.models import preguntas

# Create your views here.

def datosJson(request):

    msn={
        "usuario":"",
        "pass":""
    }
    if(request.method == 'GET' ):
        username = request.GET.get('usr')
        password = request.GET.get('pass')
        user = authenticate(request, username=username, password=password)
        if(user is not None):
            msn = {
                'usuario':user.username,
                'Nombre':user.first_name,
                'Apellido':user.last_name,
                'Correo':user.email,
                "msn":"Bienvenido",
            }
        else:
            msn={
                "msn":"Usuario o contraseña no encontrados",
                "usuario": username,
                "contra":password
            }
    
    return JsonResponse(msn)

def listpreguntas(request):
    pre = serializers.serialize('json', preguntas.objects.all())
    return HttpResponse(pre, content_type='application/json')