from django.urls import path
from . import views
from . models import Post

app_name = "blog"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("add/post/", views.add_post, name="add_post"),
    path("detail/<post_id>/", views.post_details_view, name="post_details_view"),
    path("update/<post_id>/", views.post_update_view, name="post_update_view"),
    path("delete/<post_id>/", views.post_delete_view , name="post_delete_view"),


]
