from django.urls import path

from .views import FieldListCreate, TopicListCreate, FieldUpdateDestroy, TopicUpdateDestroy

app_name = 'garden'
urlpatterns = [
    path('fields/', FieldListCreate.as_view(), name='fields'),
    path('<int:pk>/action/', FieldUpdateDestroy.as_view(), name='field-action'),
    path('<int:pk>/', TopicListCreate.as_view(), name='topics'),
    path('<int:field_pk>/<int:pk>/action/', TopicUpdateDestroy.as_view(), name='topic-action')
]
