from django.urls import path
from django.contrib.auth import views

from .views import ProfileView, signup_view

app_name = "users"
urlpatterns = [
    path('login/', views.LoginView.as_view(extra_context = {'title': 'Login'}), name='login'),
    path('logout/', views.LogoutView.as_view(extra_context = {'title': 'Logout'}), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('profile/', ProfileView.as_view(), name = 'profile')
]
