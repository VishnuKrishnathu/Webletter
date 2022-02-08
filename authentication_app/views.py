# Create your views here.
import logging

from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes, authentication_classes
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import CustomUser
import environ # importing django-environ to read env files
from django.middleware.csrf import get_token

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


@api_view(['POST'])
@parser_classes([JSONParser])
@authentication_classes([])
def register_user(request):
    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        response = Response({'message': 'User has been successfully created'}, status=status.HTTP_200_OK)
        return response

    else:
        print(user.errors)
        return Response({'message':'error saving user information. Try again'}, status=status.HTTP_406_NOT_ACCEPTABLE)


class LoginUser(APIView):
    """
    * Session based login is being implemented
    https://docs.djangoproject.com/en/4.0/topics/http/sessions/
    """
    def post(self, request, *args, **kwargs):
        username = request.data["username"]
        password = request.data["password"]
        user = CustomUser.objects.get(username=username)
        user_logged = authenticate(username=user.username, password=password)
        if user_logged:
            request.session["username"] = user.username
            login(request, user_logged)
            response = Response({
                "access": "random data"
            }, status=status.HTTP_200_OK)
            return response
        else:
            return Response({"message": "wrong user credentials has been provided"}, 401)


class LogoutUser(APIView):
    # logout functionality implemented
    # https://docs.djangoproject.com/en/4.0/topics/http/sessions/
    def get(self, request, *args, **kwargs):
        try:
            logout(request)
            del request.session["username"]

        except KeyError:
            pass
        return Response({"message": "User is now successfully logged out"}, 200)


class GetUserInfo(APIView):
    def get(self, request):
        try:
            return Response({"id": request.session["username"]}, 200)
        except KeyError:
            return Response({"message": "User is unauthorized"}, 403)


class GetCSRFToken(APIView):
    def get(self, request):
        get_token(request)
        response = Response({"message": "Token set"}, 200)
        return response
