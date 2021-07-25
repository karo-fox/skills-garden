from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from .models import Field, Topic
from .serializers import FieldSerializer, TopicSerializer


class FieldViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSerializer
    
    def get_queryset(self):
        return Field.objects.filter(owner=self.request.user)


class TopicViewset(viewsets.ModelViewSet):
    serializer_class = TopicSerializer

    def get_queryset(self):
        return Topic.objects.filter(field=self.kwargs['field_pk'])
