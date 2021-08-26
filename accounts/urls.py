from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('',index, name='index'),
    path('dashboard/',dashboard,name='dashboard'),
    path('dashboard/customer/<customer_id>',customer,name='customer'),
    path('dashboard/customer/add',add_customer,name='add_customer'),
    path('dashboard/customer/edit/<customer_id>',edit_customer,name='edit_customer'),
]