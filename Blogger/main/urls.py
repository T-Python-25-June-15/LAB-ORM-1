from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('',views.home_views, name='home_views'),
    path('add_blog/',views.add_blog_views, name='add_blog_views')
]