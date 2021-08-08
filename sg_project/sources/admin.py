from django.contrib import admin

from garden.admin import TopicLinksMixin
from users.admin import OwnerMixin

from .models import TextSource, URLSource, Source


@admin.register(Source)
class SourceAdmin(OwnerMixin, TopicLinksMixin, admin.ModelAdmin):
    list_display = ('name', 'topic_detail', 'owner')
    list_filter = ('topic', 'topic__field')

    def get_topic(self, obj):
        return obj.topic
    
    def get_owner(self, obj):
        return obj.topic.field.owner