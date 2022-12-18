from django.db import models

# Create your models here.

class Usuario(models.Model):

		TIPO_CHOICES = [
			('AD', 'Administrador'),
			('AS', "Asistente"),
			('US', 'Usuario'),
		]

		nombre = models.CharField(max_length=50)
		email = models.EmailField(max_length=50, unique=True)
		password = models.CharField(max_length=50)
		url_imagen = models.URLField(max_length=200)
		tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, default='US')
		estado = models.BooleanField(default=True)

		def __str__(self):
				return self.nombre