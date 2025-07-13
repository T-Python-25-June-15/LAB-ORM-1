from . import views
from django.urls import path

app_name='main'

urlpatterns = [
    path("",views.home_view,name="home_view"),
    path("add/",views.add_post_view, name="add_post_view"),

]