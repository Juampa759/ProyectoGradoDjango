from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_requred

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from mainapp.forms import UsuarioForm
from mainapp.models import Usuario
from django.urls import reverse, reverse_lazy
from django.contrib import messages 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin 
import io
from os import curdir, sep

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html',{
        'title': 'Inicio'
    })

def about(request):
    return render(request, 'mainapp/about.html',{
        'title': 'Sobre nosotros'
    })


def create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioForm()

    return render(request, 'mainapp/PruebaRegUsu.html',{'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if(user is not None):
            #login(request, user)
            return render(request,'mainapp/usuario.html')
        else:
            messages.warning(request,'Usuario o contraseña incorrectos')

    return render(request,'mainapp/login.html')
