from django.urls import path

from .views import FieldListCreate, TopicList

app_name = 'garden'
urlpatterns = [
    path('fields/', FieldListCreate.as_view(), name='fields'),
    path('<int:pk>/', TopicList.as_view(), name='topics')
]
