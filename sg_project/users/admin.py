from django.contrib import admin
from django.utils.safestring import mark_safe


class OwnerMixin:

    @admin.display(description='Owner')
    def owner(self, obj):
        owner = self.get_owner(obj)
        return mark_safe(f'<a href="/admin/auth/user/{owner.pk}/change/">{owner.username}</a>')
