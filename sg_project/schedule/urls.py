from django.urls import path, include

from rest_framework import routers

from .views import RevisionViewSet

router = routers.SimpleRouter()
router.register(r'revisions', RevisionViewSet, basename='revision')

app_name = 'schedule'
urlpatterns = [
    path('', include(router.urls)),
]