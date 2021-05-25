from django.urls import path

from .views import field_list_view, topic_list_view

app_name = 'garden'
urlpatterns = [
    path('fields/', field_list_view, name='fields'),
    path('<int:pk>/', topic_list_view, name='topics')
]
