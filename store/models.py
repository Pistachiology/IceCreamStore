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
			

"""class Order(models.Model):
	order_date = models.InteagerField(max_length=10)
class Product(models.Model):
	name_product = models.CharField(max_length=20)
	amount_product = models.InteagerField(max_length=5)
	price_product = models.DoubleField(max_length=5)
	score_product = models.InteagerField(max_length=5)
class Order_list(models.Model):
	id_order = models.InteagerField(max_length=10)
	id_product = models.InteagerField(max_length=10)
class Track(models):
	id_order = models.InteagerField(max_length=10)
	current_state = models.CharField(max_length=10)
	date_deliver = models.InteagerField(max_length=10)"""
