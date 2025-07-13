from django.urls import path
from . import views as main

app_name = 'main'

urlpatterns = [
    path('', main.home_view, name='home'),
    path('add_post/', main.post_create, name='post_create'),
]
