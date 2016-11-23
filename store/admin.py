from django.contrib import admin
from .models import Product, CustomUser, Order, OrderList, Tracking, Cart, VoteProduct

choices = {1:'Processing', 2:'Preparing', 3:'Delivering', 4:'Success'}

class OrderAdmin(admin.ModelAdmin):

    def show_id(self, obj):
        return "%03d" % obj.id
    show_id.short_description = 'id'

    def show_user(self, obj):
        return obj.user.username
    show_user.short_description = 'user'

    list_display = ('show_id','show_user')

class CartAdmin(admin.ModelAdmin):

    def show_id(self, obj):
        return "%03d" % obj.id
    show_id.short_description = 'id'

    def show_user(self, obj):
        return obj.user.username
    show_user.short_description = 'user'

    list_display = ('show_id', 'show_user')

class ProductAdmin(admin.ModelAdmin):
    def show_id(self, obj):
        return "%03d" % obj.id
    show_id.short_description = 'id'
    list_display = ('show_id', 'name', 'amount', 'price')
    list_display_links = ('show_id', 'name')

class TrackingAdmin(admin.ModelAdmin):

    #def show_tracking(self, obj):
    #    return ("%03d_%s" % (obj.id, obj.user.username))
    #show_tracking.short_description = 'List'

    def show_user(self, obj):
        return obj.user.username
    show_user.short_description = 'User'

    def show_state(self, obj):
        return choices[obj.current_state]
    show_state.short_description = 'State'

    def show_id(self, obj):
        return "%03d" % obj.id
    show_id.short_description = 'id'

    list_display = ('show_id', 'show_user', 'show_state')
    list_display_links = ('show_id', 'show_user')

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(CustomUser)
admin.site.register(Order, OrderAdmin)
#admin.site.register(OrderList)
admin.site.register(Tracking, TrackingAdmin)
admin.site.register(Cart, CartAdmin)
#admin.site.register(VoteProduct)
