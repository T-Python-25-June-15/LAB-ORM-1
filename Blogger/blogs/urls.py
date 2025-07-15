from django.urls import path
from . import views

app_name="blogs"

urlpatterns= [
    path("createBlogs/", views.createBlogs_view, name="createBlogs_view"),
    path("detail/<blog_id>/", views.detailBlog_view, name="detailBlog_view" ),
    path("update/<blog_id>/", views.updateBlog_view, name="updateBlog_view"),
    path("delete/<blog_id>/", views.deleteBlog_view, name="deleteBlog_view"),
]