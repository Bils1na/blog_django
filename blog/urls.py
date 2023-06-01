from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for creating a new post
    path('new_post/', views.new_post, name='new_post'),
    # Page for edit the posts
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    # Deletes post
    path('delete/<int:post_id>/', views.delete_post, name='delete'),
]