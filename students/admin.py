from django.contrib import admin
from students.models import User, preguntas, Respuestas 

# Register your models here.



admin.site.register(User)
admin.site.register(preguntas)
admin.site.register(Respuestas)
