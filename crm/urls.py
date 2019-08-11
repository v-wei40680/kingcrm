from django.urls import path, include, re_path
from crm import views

urlpatterns = [
    path('', views.dashboard, name='sales_dashboard'),
    path('stu_enrollment/', views.stu_enrollment,name='stu_enrollment'),
    re_path(r'^enrollment/(\d+)/$', views.enrollment,name='enrollment'),
    re_path(r'^enrollment/(\d+)/fileupload/$', views.enrollment_fileupload,name='enrollment_fileupload'),
    re_path(r'^stu_enrollment/(\d+)/contract_audit/$', views.contract_audit,name='contract_audit'),

]
