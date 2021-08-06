from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Field, Topic


class GardenLinksMixin:

    @admin.display(description='Topic List')
    def topic_list(self, obj):
        field = self.get_field(obj)
        return mark_safe(f'<a href="/admin/garden/topic/?field__id__exact={field.pk}">topics</a>')

    @admin.display(description='Field Detail')
    def field_detail(self, obj):
        field = self.get_field(obj)
        return mark_safe(f'<a href="/admin/garden/field/{field.id}/change/">{field.name}</a>')


@admin.register(Field)
class FieldAdmin(GardenLinksMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'topic_list',
                    'last_reviewed', 'review_frequency')
    list_display_links = ('id', 'name')
    list_filter = ('date_added',)

    def get_field(self, obj):
        return obj


@admin.register(Topic)
class TopicAdmin(GardenLinksMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'field_detail', 'last_reviewed')
    list_filter = ('field',)

    def get_field(self, obj):
        return obj.field
