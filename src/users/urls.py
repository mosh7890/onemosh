from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token

from .views import MyRegisterView, MyLoginView, MyUserDetailsView

app_name = 'users'
urlpatterns = [
    path('rest-auth/registration/', MyRegisterView, name='rest_register'),
    path('rest-auth/login/', MyLoginView, name='rest_login'),
    path('rest-auth/user/', MyUserDetailsView, name='rest_user_details'),
    path('refresh-token/', refresh_jwt_token, name='refresh_jwt_token'),
    path('verify-token/', verify_jwt_token, name='verify_jwt_token'),
]
