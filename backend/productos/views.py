from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductoSerializer
from .models import Producto


class ProductoView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
