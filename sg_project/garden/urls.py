from django.urls import path

from .views import field_list_view, topic_list_view, FieldView, HomeView

app_name = 'garden'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', FieldView.as_view(), name='field'),
    path('api/fields/', field_list_view, name='fields-list'),
    path('api/field/<int:pk>/', topic_list_view, name='topics-list')
]
