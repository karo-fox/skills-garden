from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import JsonResponse, HttpResponse

from .models import Field, Topic

class HomeView(ListView):
    template_name = 'index.html'
    model = Field

def field_list_view(request, *args, **kwargs):
    response = {
        'data': [
            {
                'name': "TEST NAME",
                'description': "TEST DESCRIPTION",
                'pk': 1
            },
            {
                'name': "TEST NAME 2",
                'description': "TEST DESCRIPTION",
                'pk': 2
            }
        ]

    }
    return JsonResponse(response)


