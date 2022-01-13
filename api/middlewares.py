import jwt
import environ   # importing django-environ to read env files
from rest_framework.response import Response

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


def jwtCheck(func):

    def validator(request):
        try:
            token = request.COOKIES['token']

            user_data = jwt.decode(token, env('ACCESS_TOKEN'), algorithms ='HS256')

            if user_data:
                request.user = user_data
                return func(request)
            else:
                return Response({'message' : 'Token expired'}, 403)

        except KeyError:

            return Response({'message': ''}, 403)

    return validator