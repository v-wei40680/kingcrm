from django.urls import path, include, re_path
from crm import views

urlpatterns = [
    path('', views.dashboard, name='sales_dashboard'),
    path('stu_enrollment/', views.stu_enrollment,name='stu_enrollment'),
    re_path(r'^enrollment/(\d+)/$', views.enrollment,name='enrollment'),
]
