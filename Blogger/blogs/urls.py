from django.urls import path
from . import views

app_name="blogs"

urlpatterns= [
    path("createBlogs/", views.createBlogs_view, name="createBlogs_view")
]