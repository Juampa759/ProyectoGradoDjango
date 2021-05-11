from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pregunta(models.Model):

    pregunta=models.TextField(verbose_name='Digite su pregunta')
    public =models.BooleanField(verbose_name='¿publico?')
    user = models.ForeignKey(User, editable=False, verbose_name="Usuario", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    edited_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"

    def __str__(self):
        return self.pregunta

class Respuesta(models.Model):

    respuesta=models.TextField(verbose_name='respuesta')
    public =models.BooleanField(verbose_name='¿publico?')
    user = models.ForeignKey(User, editable=False, verbose_name="Usuario", on_delete=models.PROTECT)
    preguntas=models.ManyToManyField(Pregunta, verbose_name="Preguntas", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    edited_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestass"

    def __str__(self):
        return self.respuesta

    
