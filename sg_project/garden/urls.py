from django.urls import path

from .views import FieldList, TopicList

app_name = 'garden'
urlpatterns = [
    path('fields/', FieldList.as_view(), name='fields-list'),
    path('<int:pk>/', TopicList.as_view(), name='topics-list')
]
