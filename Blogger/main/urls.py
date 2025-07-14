from django.urls import path
from . import views as main


app_name = 'main'

urlpatterns = [
    path('', main.home_view, name='home'),
    path('add_post/', main.post_create, name='post_create'),
    path('detail/<int:post_id>/', main.detail_view, name='detail_view'),
    path('delete/<int:post_id>/', main.delete_post, name='delete_view'),
    path('update/<int:post_id>/', main.update_post, name='update_view'),
]
