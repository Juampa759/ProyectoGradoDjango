from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.index,name="index"),
    path('index/',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('nuevo/',views.create, name="Nuevo"),
    path('login/', LoginView.as_view(template_name='mainapp/login.html'), name="login"),
    path('user/',views.login, name="usuario"),
]