from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.


@api_view(['GET'])
def get_blogs(request):
    return Response({
        "message": "Hello World"
    }, 200)


class Blogs(APIView):
    def post(self, request):
        pass
