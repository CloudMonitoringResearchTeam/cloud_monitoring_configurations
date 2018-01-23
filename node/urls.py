from django.urls import path

from . import views


app_name = 'node'

urlpatterns = [
    path('', views.create_or_delete, name='create_or_delete_node'),
    path('index', views.index, name='index'),
    path('get_father_pk', views.get_father_pk, name='get_father_pk'),
    path('add_node_view', views.add_node_view, name='add_node_view'),
    path('get_all_nodes', views.get_all_nodes, name='get_all_nodes')
]