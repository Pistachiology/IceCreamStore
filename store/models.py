from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from datetime import datetime
from django.db.models.query import EmptyQuerySet

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media/media/product_image/', default='media/media/product_image/None/no-img.jpg')
    amount = models.IntegerField()
    price = models.FloatField()
    score = models.FloatField(default=0)
    voter = models.IntegerField(default=0)
    
    
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

    def __unicode__(self):
        return self.name

class CustomUser(AbstractUser):
    address = models.CharField(max_length=300)
    tel = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    user_cart = models.ManyToManyField(Product, through='Cart')

    def purchase(self):
        if self.user_cart.all().count() == 0:
            return False
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
        return True

class VoteProduct(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    score = models.FloatField()

    def user_vote_or_update_score(self):
        obj, created = VoteProduct.objects.get_or_create(user=self.user, product=self.product)
        if created:
            self.product.score = ((self.product.score*self.product.voter) - obj.score + self.score)/self.product.voter
        else :
            temp_score = self.product.score*self.product.voter
            self.product.voter += 1
            self.product.score = (temp_score + self.score)/self.product.voter
        self.product.save()

class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    sum_price = models.FloatField()
    list_product = models.ManyToManyField(Product, through='OrderList')
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)


class OrderList(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

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

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()

    def add_or_update(self):
        obj, created = Cart.objects.update_or_create(user=self.user, product=self.product, defaults={'qty':self.qty})
        return created

class Credit(models.Model):
    cash = models.FloatField()
    code = models.CharField(max_length=16)
