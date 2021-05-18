from django.urls import path

from .views import HomeView

app_name = 'garden'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home/', HomeView.as_view(), name='home')
]
