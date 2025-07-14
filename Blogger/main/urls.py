from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('',views.home_views, name='home_views'),
    path('add_blog/',views.add_blog_views, name='add_blog_views'),
    path('detail/<blog_id>/',views.detail_views, name='detail_views'),
    path('update/<blog_id>/',views.update_views, name='update_views'),
    path('delete/<blog_id>/',views.delete_views, name='delete_views'),
]