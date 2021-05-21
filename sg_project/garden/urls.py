from django.urls import path

from .views import HomeView, field_list_view

app_name = 'garden'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home/', HomeView.as_view(), name='home'),
    path('fields/', field_list_view, name='fields'),
    # path('<int:field_pk>/<int:pk>', TopicView.as_view(), name='topic')
]
