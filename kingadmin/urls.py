from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.app_index, name='app_index'),
    re_path(r'(\w+)/(\w+)/', views.table_obj_list, name='table_obj_list'),
]
