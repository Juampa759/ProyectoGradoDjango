from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    IdUser = models.ForeignKey(User, verbose_name="Usuario", on_delete= models.CASCADE)
    pregunta = models.IntegerField(_(""))

class preguntas(models.Model):
    Pregunta = models.CharField(max_length=500)
    RespuestaA = models.CharField(max_length=200)
    RespuestaB = models.CharField(max_length=200)
    RespuestaC = models.CharField(max_length=200)
    RespuestaD = models.CharField(max_length=200)

class Respuestas(models.Model):
    IdUser = models.ForeignKey(User, verbose_name="Usuario", on_delete= models.CASCADE)
    IdPregunta = models.ForeignKey(preguntas, verbose_name="pregunta", on_delete= models.CASCADE)
    Respuesta = models.IntegerField()

