from rest_framework import viewsets

from schedule.views import RevisionMixin

from .models import Field, Topic
from .serializers import FieldSerializer, TopicSerializer


class FieldViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSerializer

    def get_queryset(self):
        return Field.objects.filter(owner_id=self.request.user.pk)


class TopicViewSet(RevisionMixin, viewsets.ModelViewSet):
    serializer_class = TopicSerializer

    def get_queryset(self):
        return Topic.objects.filter(field_id=self.kwargs['field_pk'])
