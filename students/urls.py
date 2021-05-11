from django.urls import path
from . import views

urlpatterns = [
    path('datosjson/', views.datosJson, name="datosjson"),
    path('listapreguntas/', views.listpreguntas, name="preguntas"),
]