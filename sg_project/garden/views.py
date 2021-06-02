from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

from .models import Field, Topic


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
            'review_frequency': field.review_frequency,
            'url': field.get_absolute_url()
        }
        response['fields'].append(data)
    return JsonResponse(response)


def topic_list_view(request, *args, **kwargs):
    topic_list = Topic.objects.filter(field_id = kwargs['pk'])
    response = {
        'topics': []
    }
    for topic in topic_list:
        data = {
            'pk': topic.id,
            'name': topic.name,
            'description': topic.description,
            'date_added': topic.date_added,
            'last_reviewed': topic.last_reviewed,
            'url': topic.get_absolute_url()
        }
        response['topics'].append(data)
    return JsonResponse(response)