from django.urls import path
from . import views

urlpatterns = [
    path('Pregunta/', views.preguntaJson, name="datosjson"),
    path('Siguiente/', views.sigPreJson, name="siguiente"),
]