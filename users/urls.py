from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = "users"

urlpatterns = [
    # Log in
    path('login/', views.log_in, name='login'),
    # Log out
    path('logout/', views.log_out, name='logout'),
    # Register page
    path('register/', views.register, name='register'),
    # Profile page
    path('profile/<int:user_id>/', views.profile, name='profile'),
    # Edit profile page
    path('profile/<int:user_id>/edit_profile', views.edit_profile, name='edit_profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]