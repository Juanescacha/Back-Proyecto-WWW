from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta():
        model = Post
        fields = (
            'id',
            'title',
            'description',
            'url_media',
            'is_active',
            'created_at',
        )
        read_only_fields = (
            'created_at',
        )