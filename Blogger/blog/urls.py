from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_post, name='add_post'),
    path('detail/<post_id>/', views.post_detail, name='post_detail'),
    path('update/<post_id>/', views.post_update, name='post_update'),
    path('delete/<post_id>/', views.post_delete, name='post_delete')
] 