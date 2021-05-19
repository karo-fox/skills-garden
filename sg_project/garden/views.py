from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Field, Topic

class HomeView(ListView):
    template_name = 'index.html'
    model = Field
    context_object_name = 'field_list'


class FieldView(DetailView):
    template_name = 'field.html'
    model = Field
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic_list'] = Topic.objects.filter(field_id=context['object'].id)
        return context