from django.db import models

class Post(models.Model):
	
		titulo = models.CharField(max_length=50)
		descripcion = models.CharField(max_length=200)
		url_media = models.URLField(max_length=300)
		estado = models.BooleanField(default=True)

		def __str__(self):
				return self.titulo