from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    profile_pic = models.ImageField(null=True,blank=True)
    number = models.IntegerField(null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS = (
        ('pending','pending'),
        ('For Delivery','For Delivery'),
        ('Delivered','Delivered')
    )
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    delivery_date = models.DateTimeField(default=timezone.now)
    delivery_time = models.TimeField(null=True,default=timezone.now)
    status = models.CharField(max_length=200,choices=STATUS,null=True)

    def __str__(self):
        return f'{self.customer.name} - {self.product} - {self.delivery}'