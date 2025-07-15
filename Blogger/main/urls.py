from . import views 
from django.urls import path

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("post/new/", views.add_post, name="add_post"),
    path("post/detail/<post_id>/", views.detail_post_view, name="detail_post_view"),
    path("post/update/<post_id>/", views.update_post_view, name="update_post_view"),
    path("post/delete/<post_id>/", views.delete_post_view, name="delete_post_view"),
    path("posts/all/", views.all_posts_view, name="all_posts_view"),


] 
