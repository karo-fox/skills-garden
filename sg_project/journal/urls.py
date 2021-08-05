from django.urls import path, include

from rest_framework import routers

from .views import EntryViewSet

router = routers.SimpleRouter()
router.register(r'entries', EntryViewSet, basename='entry')

app_name = 'journal'
urlpatterns = [
    path('', include(router.urls)),
]
