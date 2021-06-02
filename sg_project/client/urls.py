from django.urls import path

from .views import FieldView, HomeView

app_name = 'client'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', FieldView.as_view(), name='field')
]
