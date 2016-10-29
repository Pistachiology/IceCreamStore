from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=30)
    isAdmin = models.BooleanField()
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=60)
    address = models.CharField(max_length=300)
    tel = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    
class Product(models.Model):
    name_product = models.CharField(max_length=20)
    amount_product = models.IntegerField()
    price_product = models.FloatField(max_length=5)
    score_product = models.IntegerField()

class Order(models.Model):
    order_date = models.DateField()
    sum_price = models.FloatField()
    list_product = models.ManyToManyField(Product, through='Order_list')
    id_user = models.ForeignKey(User,on_delete=models.CASCADE)

class Order_list(models.Model):
    id_order = models.ForeignKey(Order,on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty_product = models.IntegerField()

class Tracking(models.Model):
    id_order = models.ForeignKey(Order,on_delete=models.CASCADE)
    id_user = models.ForeignKey(User,on_delete=models.CASCADE)
    STATE_CHOICE = (
        (1 , 'Processing'),
        (2 , 'Preparing'),
        (3 , 'Delivering'),
        (4 , 'Success'),
    )
    current_state = models.IntegerField(choices=STATE_CHOICE)