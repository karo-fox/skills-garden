from django.contrib import admin

from .models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('text_snippet', 'date', 'by_system', 'owner')
    list_filter = ('owner',)

    def text_snippet(self, obj):
        text_len = 25
        if len(obj.text) > text_len:
            return obj.text[:text_len] + '...'
        return obj.text
