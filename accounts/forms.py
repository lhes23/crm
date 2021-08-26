from django.db.models import fields
from django.forms import ModelForm,DateInput,TimeInput
from .models import *
from django.views.generic import CreateView

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