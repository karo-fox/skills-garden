# from django.shortcuts import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from drf_yasg.utils import swagger_auto_schema

from .serializers import RegisterSerializer


@swagger_auto_schema(method='POST', request_body=RegisterSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request, *args, **kwargs):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid()
    user = User.objects.create_user(
        username=serializer.data['username'], password=serializer.data['password'])
    user.save()
    token = Token.objects.create(user=user)
    token.save()
    return Response(serializer.data)
