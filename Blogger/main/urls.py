from django.urls import path
from . import views


app_name="main"

urlpatterns = [
    path('', views.main_view, name="main_view" ),
    path('add_post/',views.add_post, name="add_post_view")
] 