from django.contrib import admin

from garden.admin import FieldLinksMixin
from users.admin import OwnerMixin

from .models import Revision


@admin.register(Revision)
class RevisionAdmin(OwnerMixin, FieldLinksMixin, admin.ModelAdmin):
    list_display = ('date', 'field_detail', 'is_active', 'owner')
    list_filter = ('field',)

    def get_field(self, obj):
        return obj.field

    def get_owner(self, obj):
        return obj.field.owner
