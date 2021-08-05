from django.urls import path, include

from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from .views import FieldViewSet, TopicViewSet

router = routers.SimpleRouter()
router.register(r'fields', FieldViewSet, basename='field')

fields_router = nested_routers.NestedSimpleRouter(
    router, r'fields', lookup='field')
fields_router.register(r'topics', TopicViewSet, basename='topic')

app_name = 'garden'
urlpatterns = [
    path('', include(router.urls)),
    path('', include(fields_router.urls)),
]
