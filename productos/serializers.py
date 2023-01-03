from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'url_image',
            'url_origin',
            'vendor_address',
            'is_active',
            'created_at',
            'base_product',
        )
        read_only_fields = (
            'created_at',
        )