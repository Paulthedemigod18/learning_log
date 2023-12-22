"""Defines URL patterns for Users"""

from django.urls import path
from django.contrib.auth.views import LoginView
from . import views  # Import the views module from the same directory

app_name = 'users'

urlpatterns = [
    # Login page using LoginView
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Logout page
    path('logout/', views.logout_view, name='logout'),

    # Registration page
    path('register/', views.register, name='register'),
]
