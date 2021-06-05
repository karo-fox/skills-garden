from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

from rest_framework import generics
from rest_framework.response import Response

from .models import Field, Topic
from .serializers import FieldSerializer, TopicSerializer



class FieldListCreate(generics.ListCreateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer



class FieldDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FieldSerializer


    def get_queryset(self):
        queryset = Field.objects.filter(id = self.kwargs['pk'])
        return queryset



class TopicListCreate(generics.ListCreateAPIView):
    serializer_class = TopicSerializer


    def get_queryset(self, pk):
        queryset = Topic.objects.filter(field__id = pk)
        return queryset


    def list(self, request, pk):
        queryset = self.get_queryset(pk)
        serializer = TopicSerializer(queryset, many=True)
        return Response(serializer.data)