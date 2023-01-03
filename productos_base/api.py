from .models import BaseProduct
from rest_framework import viewsets, permissions
from .serializers import BaseProductSerializer

class BaseProductViewSet(viewsets.ModelViewSet):
    queryset = BaseProduct.objects.all()
    permission_classes = [
        permissions.AllowAny # ¿temporal?
    ]
    serializer_class = BaseProductSerializer