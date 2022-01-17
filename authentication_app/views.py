# Create your views here.
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes, authentication_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from .serializers import UserSerializer
import environ # importing django-environ to read env files
from webletter.settings import DEBUG

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


class LoginUser(TokenObtainPairView):
    """
    * A custom login is created to send cookies as response
    https://django-rest-framework-simplejwt.readthedocs.io/en/latest/customizing_token_claims.html
    """
    authentication_classes = ()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
