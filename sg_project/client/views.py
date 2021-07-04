from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from garden.models import Field, Topic
from garden.forms import FieldForm, TopicForm
from sources.forms import TextSourceForm, URLSourceForm



class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "home.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home"
        context['form'] = FieldForm
        return context



class FieldView(generic.DetailView):
    template_name = "field.html"
    model = Field


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Field"
        context['create_form'] = TopicForm
        context['edit_form'] = FieldForm
        return context



class TopicView(generic.DetailView):
    template_name = "topic.html"
    model = Topic


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Topic"
        context['field_pk'] = self.kwargs['field_pk']
        context['edit_form'] = TopicForm
        context['create_note_form'] = TextSourceForm
        context['create_link_form'] = URLSourceForm
        return context
 


class AboutView(generic.TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "About"
        return context