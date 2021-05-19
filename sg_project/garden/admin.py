from django.contrib import admin

from .models import Field, Topic

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_topic_filter_link', 'last_reviewed', 'review_frequency')
    list_filter = ('date_added',)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_field_link', 'last_reviewed')
    list_filter = ('field',)

