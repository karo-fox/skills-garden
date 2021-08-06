from django.contrib import admin

from garden.admin import TopicLinksMixin

from .models import TextSource, URLSource, Source


@admin.register(Source)
class SourceAdmin(TopicLinksMixin, admin.ModelAdmin):
    list_display = ('name', 'topic_detail')
    list_filter = ('topic', 'topic__field')

    def get_topic(self, obj):
        return obj.topic