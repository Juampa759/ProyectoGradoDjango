from django.contrib import admin
from students.models import preguntas, Respuesta, PregResp, RespUsu

# Register your models here.




admin.site.register(preguntas)
admin.site.register(Respuesta)
admin.site.register(PregResp)
admin.site.register(RespUsu)
