from django.urls import path
from . import views


urlpatterns = [
    path('get-blogs/', views.HandleBlog.as_view(), name="get_blogs"),
    path('post-blog/', views.HandleBlog.as_view(), name="post_blog")
]
