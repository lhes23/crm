from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('',index, name='index'),
    # Account path
    path('accounts/register/',RegisterPage,name='register'),
    path('accounts/login/',LoginPage,name='login'),
    path('accounts/logout/',LogoutPage,name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
    path('dashboard/user/',user_page, name='user_page'),
    
    # Customer Path
    path('dashboard/customer/add',add_customer,name='add_customer'),
    path('dashboard/customer/edit/<customer_id>',edit_customer,name='edit_customer'),
    path('dashboard/customer/delete/<customer_id>',delete_customer,name='delete_customer'),
    # path('dashboard/customer/search',CustomerSearchListView.as_view(),name='search_customer'),
    path('dashboard/customer/search',search_customer,name='search_customer'),
    path('dashboard/customer/<customer_id>',customer,name='customer'),
    

    # Product Path
    path('dashboard/product/add',ProductCreateView.as_view(),name='add_product'),
    path('dashboard/product/edit/<pk>',ProductUpdateView.as_view(),name='edit_product'),
    path('dashboard/product/delete/<pk>',ProductDeleteView.as_view(),name='delete_product'),
    path('dashboard/product/<pk>',ProductDetailView.as_view(),name='product'),

    # Order Path
    path('dashboard/order/add',add_order,name='add_order'),
    path('dashboard/order/edit/<order_id>',edit_order,name='edit_order'),
    path('dashboard/order/delete/<order_id>',delete_order,name='delete_order'),
]

handler404 = 'accounts.views.error_404'