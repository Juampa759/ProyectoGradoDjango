from django.shortcuts import render, HttpResponse, get_object_or_404
from save_q.models import *
from django.http import JsonResponse

# Create your views here.

def PreguntaRespuesta(request, pregunta_id):
    
    preguntas=get_object_or_404(Pregunta, id=pregunta_id)
    respuestas=Respuesta.objects.filter(preguntas=pregunta_id)


    return render(request,  'save_q/Preguntarespuesta.html',{
        
        'pregunta':preguntas,
        'respuestas': respuestas
    })

def JsonPregunta(request, pregunta_id):
    preguntas=get_object_or_404(Pregunta, id=pregunta_id)
    pre = "",preguntas
    print(preguntas)
    comments=[
        {f'pregunta: {pre}'}
    ]
    context = {'comments': comments}

    return HttpResponse(context)