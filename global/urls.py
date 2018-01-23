__author__ = 'lenovo'

from django.urls import path

from . import views


app_name = 'global'

urlpatterns = [
    path('', views.global_view, name='global_view'),
    path('conf_file', views.conf_file, name='conf_file'),
]