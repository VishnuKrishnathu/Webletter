from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('register-user', views.register_user, name="registerUser"),
    path('login-user', views.LoginUser.as_view(), name="registerUser")
]
