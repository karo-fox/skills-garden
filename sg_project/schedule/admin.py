from django.contrib import admin

from garden.admin import FieldLinksMixin

from .models import Revision


@admin.register(Revision)
class RevisionAdmin(FieldLinksMixin, admin.ModelAdmin):
    list_display = ('date', 'field_detail', 'is_active')
    list_filter = ('field',)

    def get_field(self, obj):
        return obj.field
