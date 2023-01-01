from rest_framework import serializers
from .models import BaseProduct

class BaseProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = BaseProduct
        fields = (
            'id',
            'name',
            'visit_counter',
        )