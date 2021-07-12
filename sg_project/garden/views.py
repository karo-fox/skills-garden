from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from .models import Field, Topic
from .serializers import FieldSerializer, TopicSerializer



class FieldListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, SessionAuthentication]

    queryset = Field.objects.all()
    serializer_class = FieldSerializer

    def get_queryset(self):
        queryset = Field.objects.filter(owner = self.request.user)
        return queryset



class FieldUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FieldSerializer

    def get_queryset(self):
        queryset = Field.objects.filter(id = self.kwargs['pk'])
        return queryset



class TopicListCreate(generics.ListCreateAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        queryset = Topic.objects.filter(field__id = self.kwargs['pk'])
        return queryset



class TopicUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        queryset = Topic.objects.filter(id = self.kwargs['pk'])
        return queryset