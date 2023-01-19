from django.db import models
from productos_base.models import BaseProduct

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    url_image = models.URLField(max_length=500)
    url_origin = models.URLField(max_length=500)
    vendor_address = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    base_product = models.ForeignKey(BaseProduct, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name