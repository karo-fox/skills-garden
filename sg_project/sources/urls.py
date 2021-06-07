from django.urls import path

from .views import TextSourceListCreateView, URLSourceListCreateView

app_name = 'sources'
urlpatterns = [
    path('<int:pk>/text/', TextSourceListCreateView.as_view(), name="text-list"),
    path('<int:pk>/url/', URLSourceListCreateView.as_view(), name="url-list")
]