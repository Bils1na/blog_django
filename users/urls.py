from django.urls import path, include

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
<<<<<<< HEAD
    # path('profile/<int:user_id>/edit_full_name', views.edit_full_name, name='full_name')
=======
    path('profile/<int:user_id>/edit_profile', views.edit_profile, name='edit_profile'),
>>>>>>> fedef2c92b2c58a4be05a1b9e569e1b7f00eba0b
]