from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=30)
	isAdmin = models.BooleanField()
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=60)
	address = models.CharField(max_length=300)
	tel = models.CharField(max_length=20)
	company = models.CharField(max_length=50)