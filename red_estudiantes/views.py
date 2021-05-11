from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.python.keras.models import load_model
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin 
from red_estudiantes.models import Cliente
from red_estudiantes.forms import formulario_usuario


def redes (request):
    
    dataset = pd.read_csv('Bancos.csv')
    x = dataset.iloc[:, 3:13].values 
    y = dataset.iloc[:,13].values

    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder_x_1 = LabelEncoder()
    x[:,1] = labelencoder_x_1.fit_transform(x[:,1])
    labelencoder_x_2 = LabelEncoder()
    x[:,2] = labelencoder_x_2.fit_transform(x[:,2])

    from sklearn.compose import ColumnTransformer
    columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [2])], remainder='passthrough')
    x = np.array(columnTransformer.fit_transform(x), dtype = np.float)

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)

    modelo = './modelo/modelo.h5'
    pesos_modelo = './modelo/pesos.h5'
    clasificador = load_model(modelo)
    clasificador.load_weights(pesos_modelo)

    y_pred = clasificador.predict(x_test)
    y_pred = (y_pred>0.5)

    # Matriz de Confusion
    from sklearn.metrics import confusion_matrix
    mc = confusion_matrix(y_test,y_pred)

    #probando la red neuronal
    nuevo_cliente = clasificador.predict(sc.transform(np.array([[0,1,600,0,40,3,60000,2,1,1,50000]])))


    return HttpResponse(nuevo_cliente)

class IndexView(ListView):
    template_name = 'ListaUsuarios.html'
    context_object_name = 'usuario_list'