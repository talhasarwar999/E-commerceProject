from django.utils.html import format_html
from django.contrib import admin
from order.models import *


class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "product_name",
        "user_username",
        "quantity",
        "created_at",
    ]
    list_display_links = ["id"]
    def design_code(self, obj):
        return format_html('<a href="{}/update/">{}</a>'.format(obj.pk, obj.code))

    def product_name(self, obj):
        return obj.product.title 

    def user_username(self, obj):
        return obj.user.username

    user_username.allow_tags = True
    user_username.short_description = "User" 



admin.site.register(CartItem,OrderItemAdmin)



class BillingAddressAdmin(admin.StackedInline):
    model =  BillingAddress
    extra = 1
    max_num =1

class ShippingAddressAdmin(admin.StackedInline):
    extra = 1
    max_num =1
    model =  ShippingAddress



class OrderAdmin(admin.ModelAdmin):
       
    list_display = ("id", "email", "delivery_methods", )   
    inlines = [BillingAddressAdmin,ShippingAddressAdmin]

admin.site.register(Order,OrderAdmin)


