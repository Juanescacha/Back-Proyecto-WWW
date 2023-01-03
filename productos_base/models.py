from django.db import models

# Create your models here.
class BaseProduct(models.Model):
   
    name = models.CharField(max_length=200, unique=True)
    visit_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.name