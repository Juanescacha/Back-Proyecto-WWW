from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = (
            'id',
            'name',
            'email',
            'password',
            'role',
            'is_active',
            'created_at',
        )
        read_only_fields = (
            'created_at',
        )
        lookup_field = "email"