from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('',index, name='index'),
    path('register/',RegisterPage,name='register'),
    path('login/',LoginPage,name='login'),
    path('logout/',LogoutPage,name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
    path('dashboard/customer/add',add_customer,name='add_customer'),
    path('dashboard/customer/edit/<customer_id>',edit_customer,name='edit_customer'),
    path('dashboard/customer/delete/<customer_id>',delete_customer,name='delete_customer'),
    path('dashboard/customer/<customer_id>',customer,name='customer'),

    path('dashboard/order/add',add_order,name='add_order'),
    path('dashboard/order/edit/<order_id>',edit_order,name='edit_order'),
    path('dashboard/order/delete/<order_id>',delete_order,name='delete_order'),
]