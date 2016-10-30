from django.contrib import admin
from .models import Product, CustomUser, Order, OrderList, Tracking, Cart
# Register your models here.
admin.site.register(Product)
admin.site.register(CustomUser)
admin.site.register(Order)
admin.site.register(OrderList)
admin.site.register(Tracking)
admin.site.register(Cart)
