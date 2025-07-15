# main/urls.py

from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('add/', views.add_post_view, name="add_post_view"),
    path("mode/<mode>/", views.mode_view, name="mode_view"),
    
    
    path("test/params/<int:param1>/<param2>/", views.test_params_view, name="test_params_view"),

    path("post/<int:post_id>/", views.post_detail_view, name="post_detail_view"),
    path("post/<int:post_id>/update/", views.post_update_view, name="post_update_view"),
    path("post/<int:post_id>/delete/", views.post_delete_view, name="post_delete_view"),
    
]



