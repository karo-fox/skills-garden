from rest_framework import generics
from rest_framework.response import Response

from .models import TextSource, URLSource
from .serializers import TextSourceSerializer, URLSourceSerializer



class TextSourceListCreate(generics.ListCreateAPIView):
    serializer_class = TextSourceSerializer
    
    def get_queryset(self):
        queryset = TextSource.objects.filter(topic__id = self.kwargs['pk'])
        return queryset



class TextSourceUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TextSourceSerializer

    def get_queryset(self):
        queryset = TextSource.objects.filter(id = self.kwargs['pk'])
        return queryset



class URLSourceListCreate(generics.ListCreateAPIView):
    serializer_class = URLSourceSerializer

    def get_queryset(self):
        queryset = URLSource.objects.filter(topic__id = self.kwargs['pk'])
        return queryset



class URLSourceUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = URLSourceSerializer

    def get_queryset(self):
        queryset = URLSource.objects.filter(id = self.kwargs['pk'])
        return queryset