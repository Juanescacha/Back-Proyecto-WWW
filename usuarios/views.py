from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class UserAPIView(APIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        try:
            email = request.query_params['email']
            if email != None:
                print("email:", email)
                user = User.objects.get(email=email)
                serializer = UserSerializer(user)
        except:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data)