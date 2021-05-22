from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from .models import Field, Topic

class HomeView(ListView):
    template_name = 'index.html'
    model = Field

def field_list_view(request, *args, **kwargs):
    field_list = Field.objects.all()
    response = {
        'fields': []
    }
    for field in field_list:
        data = {
            'pk': field.id,
            'name': field.name,
            'description': field.description,
            'date_added': field.date_added,
            'last_reviewed': field.last_reviewed,
            'review_frequency': field.review_frequency
        }
        response['fields'].append(data)
    return JsonResponse(response)


