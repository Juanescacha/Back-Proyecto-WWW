from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UsuarioSerializer
from .models import Usuario


class UsuarioView(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
