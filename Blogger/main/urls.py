from django.urls import path
from . import views


app_name="main"

urlpatterns = [
    path('', views.main_view, name="main_view" ),
    path('add_post/',views.add_post, name="add_post_view"),
    path('post/<int:id>/',views.post_details_view, name="post_details_view"),
    path('post/<int:id>/edit/',views.post_edit_view, name="post_edit_view"),
    path('post/<int:id>/delete/',views.post_delete_view, name="post_delete_view")
] 