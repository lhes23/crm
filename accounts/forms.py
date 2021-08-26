from django.db.models import fields
from django.forms import ModelForm
from .models import *
from django.views.generic import CreateView

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'