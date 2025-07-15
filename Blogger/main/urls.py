from . import views
from django.urls import path


app_name = 'main'

urlpatterns = [
    path("", views.home_view, name='home_view'),
    path("new_post/", views.create_post_view, name='create_post_view'),
    path("details/<int:id_post>/", views.show_details_view, name='show_details_view'),
    path("update/<int:id_post>/", views.update_post_view, name='update_post_view'),
]


