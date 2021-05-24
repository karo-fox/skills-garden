from django.urls import path

from .views import home_view, field_list_view, topic_list_view

app_name = 'garden'
urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('fields/', field_list_view, name='fields'),
    path('<int:pk>/', topic_list_view, name='topics')
    # path('<int:field_pk>/<int:pk>', TopicView.as_view(), name='topic')
]
