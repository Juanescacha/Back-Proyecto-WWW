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
            'status',
            'created_at',
        )
        read_only_fields = (
            'created_at'
        )