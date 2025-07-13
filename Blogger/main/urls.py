from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.test_view, name='test_view')
]