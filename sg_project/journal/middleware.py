from django.contrib.auth import get_user

from .models import Entry

class JournalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.log_views = ['FieldViewSet', 'TopicViewSet', 'RevisionViewSet', 'TextSourceViewSet', 'URLSourceViewSet']
        self.view_name = None
        self.entry_templates = {
            'POST': 'New OBJECT was created',
            'PUT': 'OBJECT was edited',
            'PATCH': 'OBJECT was edited',
            'DELETE': 'OBJECT was deleted',
        }
        self.objects_names = {
            'FieldViewSet': 'Field',
            'TopicViewSet': 'Topic',
            'RevisionViewSet': 'Revision',
            'TextSourceViewSet': 'Text Source',
            'URLSourceViewSet': 'URL Source',
        }
    
    def __call__(self, request):
        response = self.get_response(request)
        if self.view_name in self.log_views and request.method in self.entry_templates.keys():
            message = self.get_message(request.method)
            self.create_entry(message, request.user)
        return response
    
    def get_message(self, method):
        message = self.entry_templates[method]
        o_name = self.objects_names[self.view_name]
        message = message.replace('OBJECT', o_name)
        return message
    
    def create_entry(self, text, owner):
        entry = Entry.objects.create(text=text, owner=owner)
        entry.save()
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        self.view_name = str(view_func.__name__)
        return None
