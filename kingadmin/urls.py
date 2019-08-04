from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.app_index, name='app_index'),
    re_path(r'^(\w+)/(\w+)/(\d+)/change/$', views.table_obj_change,name='table_obj_change'),
    re_path(r'^(\w+)/(\w+)/add/$', views.table_obj_add,name='table_obj_add'),
    re_path(r'(\w+)/(\w+)/', views.table_obj_list, name='table_obj_list'),
]
