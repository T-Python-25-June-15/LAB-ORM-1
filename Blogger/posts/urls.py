from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('create/',views.create_posts, name="create_posts")
]