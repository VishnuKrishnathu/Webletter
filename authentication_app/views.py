# Create your views here.
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes, authentication_classes
from rest_framework.views import APIView
# from rest_framework_simplejwt.views import TokenRefreshView
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
        if authenticate(username=user.username, password=password):
            request.session["user_id"] = user.id
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
            del request.session["user_id"]

        except KeyError:
            pass
        return Response({"message": "User is now successfully logged out"}, 200)


class GetUserInfo(APIView):
    def get(self, request):
        try:
            return Response({"id": request.session["user_id"]}, 200)
        except KeyError:
            return Response({"message" : "User is unauthorized"}, 403)


"""
class RefreshToken(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={"refresh": request.COOKIES["token"]})

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
"""


class GetCSRFToken(APIView):
    def get(self, request):
        print(get_token(request))
        return Response({"message": "Token set"}, 200)
