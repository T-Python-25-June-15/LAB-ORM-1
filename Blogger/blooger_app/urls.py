from django.urls import path
from . import views

app_name = 'blogger_app'


urlpatterns = [
    path("create", views.blogg_view, name="blogg_view"),
    path("detail/<blogg_id>", views.blogg_detail_view, name="blogg_detail_view"),
    path("update/<blogg_id>",views.blogg_update_view, name="blogg_update_view"),
    path("delete/<blogg_id>",views.blogg_delete_view, name="blogg_delete_view"),
]