from django.db import models
from django.contrib.auth.models import User


class preguntas(models.Model):
    Pregunta = models.CharField(max_length=500)
    Descripcion = models.CharField(max_length=500)

class Respuesta(models.Model):
    respuesta = models.CharField(max_length=500)
    Descripcion = models.CharField(max_length=500)

class PregResp(models.Model):
    IdPregunta = models.ForeignKey(preguntas, verbose_name="Pregunta", on_delete= models.CASCADE)
    IdRespuesta =models.ForeignKey(Respuesta, verbose_name="Respuesta", on_delete= models.CASCADE)

class RespUsu(models.Model):
    IdUser = models.ForeignKey(User, verbose_name="Usuario", on_delete= models.CASCADE)
    IdPregunta = models.ForeignKey(preguntas, verbose_name="Pregunta", on_delete= models.CASCADE)
    IdRespuesta =models.ForeignKey(Respuesta, verbose_name="Respuesta", on_delete= models.CASCADE)

