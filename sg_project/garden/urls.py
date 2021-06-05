from django.urls import path

from .views import FieldListCreate, TopicListCreate, FieldUpdateDestroy

app_name = 'garden'
urlpatterns = [
    path('fields/', FieldListCreate.as_view(), name='fields'),
    path('<int:pk>/action/', FieldUpdateDestroy.as_view(), name='field'),
    path('<int:pk>/', TopicListCreate.as_view(), name='topics')
]
