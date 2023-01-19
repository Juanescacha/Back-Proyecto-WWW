from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
