from django.shortcuts import render
from django.views.generic import ListView

from .models import Field, Topic

class HomeView(ListView):
    template_name = 'index.html'
    queryset = Field.objects.all()


class FieldView(ListView):
    template_name = 'field.html'