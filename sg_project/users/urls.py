from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from .views import register, login

app_name = 'users'
urlpatterns = [
    path('register/', register, name='register'),
    path('token/', ObtainAuthToken.as_view(), name='token')
]
