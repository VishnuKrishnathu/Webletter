from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blogs

# Create your views here.


class HandleBlog(APIView):
    def get(self, request):
        return Response({
            "message": "Hello World"
        }, 200)

    def post(self, request):
        blog = Blogs(
            title=request.data["title"],
            summary=request.data["summary"],
            article=request.data["article"]
        )
        blog.user = request.user
        blog.save()

        return Response({
            "message": "data successfuly stored"
        }, 200)
