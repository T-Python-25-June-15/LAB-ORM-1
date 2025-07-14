from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('add/post/', views.add_view, name='add_view'),
    path('details/<post_id>/', views.detail_view, name='detail_view'),
    path('update/<post_id>/', views.update_view, name='update_view'),
    path('delete/<post_id>/', views.delete_view, name='delete_view'),
] 