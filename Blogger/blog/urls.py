from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("add/post/", views.add_post, name="add_post"),

]
