from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.http import HttpResponse
from students.models import preguntas, Respuesta, PregResp, RespUsu
from pregPrueba.models import person

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
        #aqui creo el id de la pregunta del usuario y su score
        if(user is not None):
            try:
                usur = person.objects.get(User_id=user.id)
            except:
                persona = person(pregunta = 1,User_id=user.id, score = 0)
                persona.save()
            msn = {
                'id':user.id,
                'usuario':user.username,
                'Nombre':user.first_name,
                'Apellido':user.last_name,
                'Correo':user.email,
                'score':usur.score,
                'pregunta':usur.pregunta,
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
    preguntaid = request.GET.get('id')
    pre = serializers.serialize('json', PregResp.objects.filter(IdPregunta_id=preguntaid))
    
    print (pre[100:150])

    return HttpResponse(pre, content_type='application/json')


def pregJson(request):

    msn={
        "usuario":"",
        "pass":""
    }
    
    if(request.method == 'GET'):        
        preguntaid = request.GET.get('id')

        pregunta = PregResp.objects.get(IdPregunta_id=preguntaid, IdRespuesta_id= 2)

        if(pregunta is not None):
            msn={
                'id':pregunta.id,
                'pregunta': pregunta.IdPregunta_id,
                'Respuesta': pregunta.IdRespuesta_id,
          
            }
            #return redirect('index')
        else:
            msn={'msn':'Usuario o contraseña incorrectos'}

    

    return JsonResponse(msn)