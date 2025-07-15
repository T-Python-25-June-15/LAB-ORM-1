from . import views
from django.urls import path

app_name = "blogs"

urlpatterns = [
    path('',views.add_blog, name="add_blog_new"),
    path('detail/<blog_id>/',views.blog_detail_view, name="blog_detail_view"),
    path('update/<blog_id>/',views.blog_update_view, name="blog_update_view"),
    path('delete/<blog_id>/',views.blog_delete_view, name="blog_delete_view"),
]
