from django.urls import path, include

from rest_framework import routers

from .views import TextSourceViewSet, URLSourceViewSet

router = routers.SimpleRouter()
router.register(r'(?P<topic_pk>[^/.]+)/text', TextSourceViewSet, basename='text-source')
router.register(r'(?P<topic_pk>[^/.]+)/url', URLSourceViewSet, basename='url-source')

app_name = 'sources'
urlpatterns = [
    path('', include(router.urls)),
]