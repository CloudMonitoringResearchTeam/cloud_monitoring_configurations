from django.urls import path

from . import views


app_name = 'node'

urlpatterns = [
    path('', views.create_or_delete, name='create_or_delete_node'),
    path('index', views.index, name='index'),
    path('prometheus_file', views.read_or_write_prometheus_conf_file, name='read_or_write_prometheus_conf_file'),
    path('alert_rule', views.read_or_write_alert_rule, name='read_or_writ_alert_rule'),
    path('alert_file', views.read_or_write_alert_conf_file, name='read_or_write_alert_conf_file'),
    path('get_father_pk', views.get_father_pk, name='get_father_pk')
]