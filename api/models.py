from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(models.Model):
   
    class Role(models.TextChoices):
        CLIENT_ROLE = "client", _('client')
        ASSISTANT_ROLE = "assistant", _('assistant')
        ADMINISTRATOR_ROLE = "administrator", _('administrator')

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(
        max_length=15,  
        choices=Role.choices,
        default=Role.CLIENT_ROLE
    )
    is_active = models.BooleanField(default=True)