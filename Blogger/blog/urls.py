from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path("create/", views.create_post_view , name="create_post_view"),
    path("deleteall/", views.delete_all_objects_view , name="delete_all_objects_view"),
    path("details/<blog_id>/" , views.blog_detail_view ,name="blog_detail_view" ),
    path("update/<blog_id>/" , views.blog_update_view ,name="blog_update_view" ),
    path("delete/<blog_id>/" , views.delete_blog_view ,name="delete_blog_view" )

 ]
