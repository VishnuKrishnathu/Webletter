# Create your views here.
from django.db import reset_queries
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from django.contrib.auth import authenticate
from .serializers import UserSerializer
import jwt
import environ    # importing django-environ to read env files
from webletter.settings import DEBUG


# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


@api_view(['POST'])
@parser_classes([JSONParser])
def registerUser(request):
    user = UserSerializer(data = request.data)
    if(user.is_valid()):
        user.save()
        encoded_jwt = jwt.encode({
            "username": user.data['username'],
        }, env('ACCESS_TOKEN'), algorithm='HS256')

        response = Response({'message': 'User has been successfully created'}, status=200)
        response.set_cookie(key="token", value=encoded_jwt, max_age=60*60*24, httponly=True, secure=not(DEBUG))
        return response

    else:
        print(user.errors)
        return Response({'message' : 'error saving user informaton. Try again'}, 400)


@api_view(['POST'])
@parser_classes([JSONParser])
def loginUser(request):
    data = request.data
    user = authenticate(
        username = data['username'],
        password = data['password']
    )
    print(user)
    try:
        token = request.COOKIES['token']
        print(token)
        user_data = jwt.decode(token, env('ACCESS_TOKEN'), algorithms ='HS256')

        if (user_data["username"] != data["username"]):
            if (user == None):
                return Response({'message' : 'Check the login credentials and try again'}, 400)

            else:
                return Response({'message' : 'User is now successfully logged in'}, 200)

    except KeyError:
        encoded_jwt = jwt.encode({
            "username": data['username'],
        }, env('ACCESS_TOKEN'), algorithm='HS256')

        response = Response({'message' : 'User is now successfully logged in'}, 200)
        response.set_cookie(key="token", value=encoded_jwt, max_age=60*60*24, httponly=True, secure=not(DEBUG))

        return response
