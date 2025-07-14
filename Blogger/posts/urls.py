from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('update/<int:post_id>/', views.update_post, name='update_post'),
    path('add/', views.add_post, name='add_post'), 
]