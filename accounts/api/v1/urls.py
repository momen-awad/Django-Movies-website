from django.urls import path
from .views import signup

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/v1/login', obtain_auth_token, name="api_login"),
    path('api/v1/signup', signup, name="signup")

]