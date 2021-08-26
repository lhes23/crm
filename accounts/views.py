from django import forms
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages

def index(request):
    return render(request,'accounts/index.html')

def dashboard(request):
    context = {
        'customers_count':Customer.objects.count(),
        'customers':Customer.objects.all(),
        'products_count':Product.objects.count(),
        'products':Product.objects.all(),
        'orders_count':Order.objects.count(),
        'orders':Order.objects.all().order_by('delivery')
    }
    template = 'accounts/dashboard.html'
    return render(request,template,context)

def customer(request,customer_id):
    context = {'customer':Customer.objects.get(pk=customer_id)}
    template = 'accounts/customer/customer.html'
    return render(request,template,context)

def add_customer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Customer Successfully Added')
        return redirect('accounts:dashboard')
    context = {'form':form}
    template = 'accounts/customer/add_customer.html'
    return render(request,template,context)

def edit_customer(request,customer_id):
    customer = Customer.objects.get(pk=customer_id)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        messages.success(request,'Customer Successfully Updated')
        return redirect('accounts:customer',customer_id)
    context = {'form':form}
    template = 'accounts/customer/add_customer.html'
    return render(request,template,context)

def delete_customer(request,customer_id):
    customer = Customer.objects.get(pk=customer_id)
    if request.method == 'POST':
        customer.delete()
        messages.success(request,f'{customer.name} has been successfully deleted')
        return redirect('accounts:dashboard')
    context = {'customer':customer}
    template = 'accounts/customer/delete_customer.html'
    return render(request,template,context)


def add_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Order Successfully Added')
        return redirect('accounts:dashboard')
    context = {'form':form}
    template = 'accounts/order/add_order.html'
    return render(request,template,context)

def edit_order(request,order_id):
    order = Order.objects.get(pk=order_id)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        messages.success(request,'Order Successfully Updated')
        return redirect('accounts:dashboard')
    context = {'form':form}
    template = 'accounts/order/add_order.html'
    return render(request,template,context)

def delete_order(request,order_id):
    order = Order.objects.get(pk=order_id)
    if request.method == 'POST':
        order.delete()
        messages.success(request,f'{order.id} has been successfully deleted')
        return redirect('accounts:dashboard')
    context = {'order':order}
    template = 'accounts/order/delete_order.html'
    return render(request,template,context)