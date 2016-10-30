from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    address = models.CharField(max_length=300)
    tel = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    
class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='product_image', default='product_image/None/no-img.jpg')
    amount = models.IntegerField()
    price = models.FloatField(max_length=5)
    score = models.FloatField()
    
    def add_or_update(self):
        defaults = {
            'name':self.name,
            'description':self.description,
            'image':self.image,
            'amount':self.amount,
            'price':self.price,
            'score':self.score    
        }
        obj, created = Product.objects.update_or_create(id=self.id,defaults=defaults)
        return created

    def delete(self):
        Product.objects.get(id=self.id).delete()

class Order(models.Model):
    date = models.DateField()
    sum_price = models.FloatField()
    list_product = models.ManyToManyField(Product, through='OrderList')
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

class OrderList(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()

class Tracking(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    STATE_CHOICE = (
        (1 , 'Processing'),
        (2 , 'Preparing'),
        (3 , 'Delivering'),
        (4 , 'Success'),
    )
    current_state = models.IntegerField(choices=STATE_CHOICE)
