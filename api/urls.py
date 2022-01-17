from django.urls import path
from . import views


urlpatterns = [
    path('get-blogs', views.get_blogs)
]