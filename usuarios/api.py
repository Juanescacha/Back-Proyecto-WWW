from .models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

from rest_framework.response import Response
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny # ¿temporal?
    ]
    serializer_class = UserSerializer
    lookup_field = "email"
    lookup_value_regex = "[^/]+"

    """ def get_queryset(self):
        users = User.objects.all()
        return users    
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print("params:",params)

        return Response({}) """