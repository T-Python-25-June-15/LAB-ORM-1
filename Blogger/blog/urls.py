from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path("create/", views.create_post_view , name="create_post_view"),
    path("delete/", views.delete_all_objects_view , name="delete_all_objects_view"),

 ]
