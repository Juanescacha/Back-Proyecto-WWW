from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(models.Model):
   
    class Role(models.TextChoices):
        CLIENT_ROLE = "client", _("client")
        ASSISTANT_ROLE = "assistant", _("assistant")
        ADMINISTRATOR_ROLE = "administrator", _("administrator")

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(
        max_length=13,  
        choices=Role.choices,
        default=Role.CLIENT_ROLE,
    )

    def __str__(self):
        return self.email