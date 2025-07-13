from django.urls import path
from . import views

app_name = 'blogger_app'


urlpatterns = [
    path("", views.blogg_view, name="blogg_view"),
]