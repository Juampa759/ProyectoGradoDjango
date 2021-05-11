from django.urls import path
from . import views
urlpatterns = [
    path('listar/',views.IndexView.as_view() ,name='Lista'),
]