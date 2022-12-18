from django.db import models


class Producto(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    url_imagen = models.URLField(max_length=300)
    url_origen = models.URLField(max_length=300)
    direccion_proveedor = models.JSONField()
    vistas = models.IntegerField(default=0)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
