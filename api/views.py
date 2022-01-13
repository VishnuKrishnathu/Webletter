from rest_framework.response import Response
from rest_framework.decorators import api_view
from .middlewares import jwtCheck

# Create your views here.

@api_view(['GET'])
@jwtCheck
def getBlogs(request):

    return Response({
        "message" : "Hello World"
    }, 200)