# Create your views here.
import io
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .serializers import UserSerializer
import jwt
import json
import environ   # importing django-environ to read env files


# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


### converts JSON object to python data type
def JSONToDict(json_object):
    stream = io.BytesIO(json_object)
    data = JSONParser().parse(stream)
    return data

def DictToBString(dict_object):
    return str(json.dumps(dict_object).encode('utf-8'))



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

        response = Response({'message': 'User has been successfully created'})
        response.set_cookie(key="token", value=encoded_jwt, max_age=60*60*24, httponly=True)
        return response

    else:
        return Response({'message' : 'error saving user informaton. Try again'}, 400)


@api_view(['POST'])
def loginUser(request):
    data = JSONToDict(request.body)
    user = authenticate(
        username = data['username'],
        password = data['password']
    )

    print(user)
    if user == None:
        return Response({'message' : 'Check the login credentials and try again'}, 400)

    else:
        return Response({'message' : 'User is now successfully logged in'}, 200)