from django.urls import path

from .views import TextSourceListCreate, URLSourceListCreate, TextSourceUpdateDestroy, URLSourceUpdateDestroy

app_name = 'sources'
urlpatterns = [
    path('<int:pk>/text/', TextSourceListCreate.as_view(), name="text-list"),
    path('<int:pk>/url/', URLSourceListCreate.as_view(), name="url-list"),
    path('<int:pk>/text/action/', TextSourceUpdateDestroy.as_view(), name="text-action"),
    path('<int:pk>/url/action/', URLSourceUpdateDestroy.as_view(), name="url-action")
]