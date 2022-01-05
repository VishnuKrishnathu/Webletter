from django.shortcuts import render

# Create your views here.
import io
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
import jwt
import environ   # importing django-environ to read env files


# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


### converts JSON object to python data type
def JSONToDict(json_object):
    stream = io.BytesIO(json_object)
    data = JSONParser().parse(stream)
    return data


@api_view(['POST'])
def registerUser(request):
    user = UserSerializer(data = JSONToDict(request.body))
    if(user.is_valid()):
        user.save()
        encoded_jwt = jwt.encode({
            "username": user.data['username'],
            "password": user.data['password'],
            "email": user.data['password']
        }, env('ACCESS_TOKEN'))
        return Response({'token' : encoded_jwt}, 200)

    else:
        return Response({'message' : 'error saving user informaton. Try again'}, 400)


@api_view(['POST'])
def loginUser(request):
    pass