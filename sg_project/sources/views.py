from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

from .models import TextSource, URLSource
from .serializers import TextSourceSerializer, URLSourceSerializer


class TextSourceViewSet(viewsets.ModelViewSet):
    serializer_class = TextSourceSerializer

    def get_queryset(self):
        return TextSource.objects.filter(topic__id = self.kwargs['topic_pk'])


class URLSourceViewSet(viewsets.ModelViewSet):
    serializer_class = URLSourceSerializer

    def get_queryset(self):
        return URLSource.objects.filter(topic__id = self.kwargs['topic_pk'])
