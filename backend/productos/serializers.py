from rest_framework import serializers
from .models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            "id",
            "nombre",
            "precio",
            "url_imagen",
            "url_origen",
            "direccion_proveedor",
            "vistas",
            "estado",
        )
