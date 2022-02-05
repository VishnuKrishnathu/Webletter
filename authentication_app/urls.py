from django.urls import path
from . import views

urlpatterns = [
    path('register-user', views.register_user, name="registerUser"),
    path('login-user', views.LoginUser.as_view(), name="registerUser"),
    path('logout-user', views.LogoutUser.as_view(), name='token_refresh'),
    path('get-user', views.GetUserInfo.as_view(), name="user_information"),
    path('get-csrf', views.GetCSRFToken.as_view(), name="get_csrf_token")
]
