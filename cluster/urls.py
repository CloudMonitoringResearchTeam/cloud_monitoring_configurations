__author__ = 'lenovo'


from django.urls import path

from . import views


app_name = 'cluster'

urlpatterns = [
    path('', views.cluster_view, name='cluster_view'),
    path('conf_file', views.conf_file, name='conf_file'),
]