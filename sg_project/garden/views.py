from django.http import JsonResponse

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
            'review_frequency': field.review_frequency
        }
        response['fields'].append(data)
    response["Access-Control-Allow-Origin"] = "*"
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
            'last_reviewed': topic.last_reviewed
        }
        response['topics'].append(data)
    return JsonResponse(response)