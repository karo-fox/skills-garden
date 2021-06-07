from rest_framework import generics
from rest_framework.response import Response

from .models import TextSource, URLSource
from .serializers import TextSourceSerializer, URLSourceSerializer



class TextSourceListCreateView(generics.ListCreateAPIView):
    serializer_class = TextSourceSerializer
    
    def get_queryset(self):
        queryset = TextSource.objects.filter(topic__id = self.kwargs['pk'])
        return queryset



class URLSourceListCreateView(generics.ListCreateAPIView):
    serializer_class = URLSourceSerializer

    def get_queryset(self):
        queryset = URLSource.objects.filter(topic__id = self.kwargs['pk'])
        return queryset
