from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CustomUser

@api_view(['POST'])
def registerUser(request):

    username = request.data['username']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    email = request.data['email']
    password = request.data['password']
    user = CustomUser(username = username, first_name = first_name, last_name= last_name, email = email, password = password)
    print(user)

    user.save()


    return Response({
        "message" : "Hello World"
    }, 200)