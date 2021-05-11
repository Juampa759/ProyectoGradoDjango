from django.contrib import admin
from .models import *

# Register your models here.

class PreguntaAdmin(admin.ModelAdmin):
    readonly_fields=('user','created_at','edited_at',)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id=request.user.id
        
        obj.save()

class RespuestaAdmin(admin.ModelAdmin):
    readonly_fields=('user','created_at','edited_at',)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id=request.user.id
        
        obj.save()


admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
