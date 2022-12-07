#from django.shortcuts import render
#from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

from . import models



# Create your views here.

def hello(request):
    return HttpResponse("Hello world")

def about(request):
    return HttpResponse('<h1>Esto es un about vacío</h1>')

class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0): #se asume que solo encontrará un usuario con ése id
            users = list(models.User.objects.filter(id=id).values()) 
            if len(users) > 0:
                res = {'message': 'Success', 'user':users[0]}
            else:
                res = {'message': 'User not found'}  
        else: 
            users = list(models.User.objects.values())
            if len(users) > 0:
                res = {'message': 'Success', 'users':users}
            else:
                res = {'message': 'Users not found'}  
        return JsonResponse(res)

    def post(self, request):
        res = {'message': 'success'}  
        data = json.loads(request.body)
        print(data)
        models.User.objects.create(
            email=data['email'],
            password=data['password'],
            name=data['name'],
            role=data['role']
        )
        return JsonResponse(res)

    def put(self, request, id):
        data = json.loads(request.body)
        users = list(models.User.objects.filter(id=id).values()) 
        if len(users) > 0:
            user = models.User.objects.get(id=id)
            user.name = data['name']
            user.email = data['email']
            user.password = data['password']
            
            if 'is_active' in data.keys():
                user.is_active = data['is_active']
            user.save()
            res = {'message': 'success'}  
        else:
            res = {'message': 'user not found'}  

        return JsonResponse(res)

    def delete(self, request, id):
        users = list(models.User.objects.filter(id=id).values()) 
        if (len(users) > 0):
            models.User.objects.filter(id=id).delete()  
            res = {'message': 'success'}  
        else:
            res = {'message': 'user not found'}  

        return JsonResponse(res)