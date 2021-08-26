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
        'orders':Order.objects.all()
    }
    return render(request,'accounts/dashboard.html',context)

def add_customer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Customer Successfully Added')
        return redirect('accounts:dashboard')
    context = {'form':form}
    return render(request,'accounts/add_customer.html',context)
