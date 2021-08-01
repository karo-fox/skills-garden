from rest_framework import viewsets

from .models import Revision
from .serializers import RevisionSerializer


class RevisionViewSet(viewsets.ModelViewSet):
    serializer_class = RevisionSerializer

    def get_queryset(self):
        return Revision.objects.filter(field__owner=self.request.user)