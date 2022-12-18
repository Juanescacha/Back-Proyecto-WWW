from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
