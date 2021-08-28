from django.contrib.auth import forms
from django.db.models import fields
from django.forms import ModelForm,DateInput,TimeInput, widgets
from .models import *
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class DateInput(DateInput):
    input_type = 'date'

class TimeInput(TimeInput):
    input_type = 'time'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'delivery_date':DateInput(),
            'delivery_time':TimeInput
        }

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
