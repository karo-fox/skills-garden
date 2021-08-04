import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from garden.models import Field, Topic
from garden.serializers import TopicSerializer

from .models import Revision
from .serializers import RevisionSerializer


class RevisionViewSet(viewsets.ModelViewSet):
    serializer_class = RevisionSerializer

    def get_queryset(self):
        return Revision.objects.filter(field__owner=self.request.user)


class RevisionMixin(object):

    @action(methods=['post', 'get'], detail=True)
    def revise(self, request, *args, **kwargs):
        topic = Topic.objects.filter(pk=kwargs['pk'])[0]
        field = Field.objects.filter(pk=kwargs['field_pk'])[0]
        self.set_last_reviewed_today([topic, field])
        rev_date = self.get_revision_date(field)
        self.create_revision(rev_date, field)
        data = TopicSerializer(topic).data
        return Response(data)

    def set_last_reviewed_today(self, objects):
        for o in objects:
            o.last_reviewed = datetime.date.today()
            o.save()
    
    def get_revision_date(self, field):
        interval = datetime.timedelta(days=field.review_frequency)
        date = datetime.date.today() + interval
        return date
    
    def create_revision(self, date, field):
        revision = Revision(date=date, field=field)
        revision.save()