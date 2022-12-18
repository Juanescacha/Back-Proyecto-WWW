from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
		list_display = ('nombre', 'precio', 'url_imagen', 'url_origen', 'direccion_proveedor', 'vistas', 'estado')

admin.site.register(Producto, ProductoAdmin)