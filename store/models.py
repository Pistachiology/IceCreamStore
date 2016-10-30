from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='product_image', default='product_image/None/no-img.jpg')
    amount = models.IntegerField()
    price = models.FloatField()
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

class CustomUser(User):
    address = models.CharField(max_length=300)
    tel = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    cart = models.ManyToManyField(Product, through='Cart')

    def purchase(self):
        order = Order(user_id=self.id,sum_price=0)
        order.save()
        for item in self.cart:
            product = Product.objects.get(id=item.product_id)
            order.sum_price = item.qty * product.price
            product.amount -= item.qty
            product.add_or_update()
            OrderList(user_id=item.user_id, product_id=item.product_id, qty=item.qty).save()
        self.cart.clear()
        order.save()
    
class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    sum_price = models.FloatField()
    list_product = models.ManyToManyField(Product, through='OrderList')
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class OrderList(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()

class Tracking(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    STATE_CHOICE = (
        (1 , 'Processing'),
        (2 , 'Preparing'),
        (3 , 'Delivering'),
        (4 , 'Success'),
    )
    current_state = models.IntegerField(choices=STATE_CHOICE)

class Cart(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()

    def add_or_update(self):
        obj, created = Cart.objects.update_or_create(user_id=self.user_id, product_id=self.product_id, defaults={'qty':self.qty})
        return created
    def delete(self):
        Cart.objects.get(user_id=self.user_id, product_id=self.product_id).delete()
