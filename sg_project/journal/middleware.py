import re

from django.contrib.auth import get_user

from .models import Entry


class JournalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.log_views = ['FieldViewSet', 'TopicViewSet',
                          'RevisionViewSet', 'TextSourceViewSet', 'URLSourceViewSet']
        self.view_name = None
        self.entry_templates = {
            'POST': 'New OBJECT was created',
            'PUT': 'OBJECT was edited',
            'PATCH': 'OBJECT was edited',
            'DELETE': 'OBJECT was deleted',
        }
        self.types = {
            'FieldViewSet': 'Field',
            'TopicViewSet': 'Topic',
            'RevisionViewSet': 'Revision',
            'TextSourceViewSet': 'Text Source',
            'URLSourceViewSet': 'URL Source',
        }
        self.object_name = None

    def __call__(self, request):
        response = self.get_response(request)
        if self.view_name in self.log_views and request.method in self.entry_templates.keys():
            self.create_entry(request.method, request.user)
        return response

    def create_entry(self, method, owner):
        message = self.get_message(method)
        entry = Entry.objects.create(text=message, owner=owner)
        entry.save()

    def get_message(self, method):
        message = self.entry_templates[method]
        o_type = self.types[self.view_name]
        message = message.replace('OBJECT', o_type)
        return message

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method in self.entry_templates.keys():
            if 'revise' in request.path:
                self.view_name = 'RevisionViewSet'
            else:
                self.view_name = str(view_func.__name__)
        return None
