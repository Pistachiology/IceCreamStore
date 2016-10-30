from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from datetime import datetime
from django.db.models.query import EmptyQuerySet

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media/product_image/', default='media/product_image/None/no-img.jpg')
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

class CustomUser(AbstractUser):
    address = models.CharField(max_length=300)
    tel = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    user_cart = models.ManyToManyField(Product, through='Cart')

    def purchase(self):
        if self.user_cart.all().count() == 0:
            return
        order = Order(user=self,sum_price=0)
        order.save()
        for product in self.user_cart.all():
            item = Cart.objects.get(user=self, product=product)
            order.sum_price += item.qty * product.price
            product.amount -= item.qty
            product.add_or_update()
            OrderList(order=order, product=product, qty=item.qty).save()
        self.user_cart.clear()
        order.save()
    
class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    sum_price = models.FloatField()
    list_product = models.ManyToManyField(Product, through='OrderList')
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class OrderList(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()

class Tracking(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    STATE_CHOICE = (
        (1 , 'Processing'),
        (2 , 'Preparing'),
        (3 , 'Delivering'),
        (4 , 'Success'),
    )
    current_state = models.IntegerField(choices=STATE_CHOICE, default=1)

    def add_or_update(self):
        obj, created = Tracking.objects.update_or_create(order=self.order, user=self.user, defaults={'current_state':current_state})
    def delete(self):
        Tracking.objects.get(order=self.order, user=self.user).delete()

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()

    def add_or_update(self):
        obj, created = Cart.objects.update_or_create(user=self.user, product=self.product, defaults={'qty':self.qty})
        return created
    def delete(self):
        Cart.objects.get(user=self.user, product=self.product).delete()
