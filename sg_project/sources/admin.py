from django.contrib import admin

from .models import TextSource, URLSource

admin.site.register(TextSource)
admin.site.register(URLSource)
