from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
  path('', views.home, name='home'),
  path('add/' ,views.add_post, name='add_post'),
  path("detail/<int:blog_id>/" , views.blog_detail_view , name = "blog_detail_view"),
  path("update/<int:blog_id>/", views.blog_update_view , name = "blog_update_view"),
  path("delete/<int:blog_id>/", views.blog_delete_view , name = "blog_delete_view")

]