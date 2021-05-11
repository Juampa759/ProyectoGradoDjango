from django.urls import path
from . import views

urlpatterns = [
    path('datos/<int:pregunta_id>',views.PreguntaRespuesta,name="datos"),
    path('json/<int:pregunta_id>', views.JsonPregunta),
    
]