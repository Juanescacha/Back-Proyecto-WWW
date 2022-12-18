from django.contrib import admin
from .models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "password", "url_imagen", "tipo", "estado")


admin.site.register(Usuario, UsuarioAdmin)
