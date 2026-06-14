from django.contrib import admin
from .models import Proyecto, Habilidad, Mensaje


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "destacado", "orden", "fecha"]
    list_editable = ["destacado", "orden"]


@admin.register(Habilidad)
class HabilidadAdmin(admin.ModelAdmin):
    list_display = ["nombre", "categoria", "nivel", "orden"]
    list_editable = ["nivel", "orden"]
    list_filter = ["categoria"]


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ["nombre", "email", "asunto", "fecha", "leido"]
    list_filter = ["leido"]
    readonly_fields = ["nombre", "email", "asunto", "mensaje", "fecha"]
