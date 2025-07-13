from . import views
from django.urls import path

app_name = "blogs"

urlpatterns = [
    path('',views.add_blog, name="add_blog_new"),
]
