from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(models.Model):
   
    ROLE_CHOICES = [
        ('AD', 'administrator'),
        ('AS', 'assistant'),
        ('CL', 'client'),
    ]

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(
        max_length=2,  
        choices=ROLE_CHOICES,
        default='CL'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name