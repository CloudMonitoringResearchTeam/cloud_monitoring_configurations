from django.urls import path

from . import views


app_name = 'user'

urlpatterns = [
    path('', views.create_or_get_single, name='create_or_get_single'),
    # path('<int:user_id>/', views.get_single, name='get_single'),
    path('password/', views.change_password, name='change_password')
]