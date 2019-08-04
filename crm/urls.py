from django.urls import path, include
from crm import views

urlpatterns = [
    path('', views.dashboard, name='sales_dashboard'),
]
