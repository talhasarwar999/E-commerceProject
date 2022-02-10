from django.contrib.auth import get_user_model
from django.utils.translation import to_language
from product.models import Product
from django.conf import settings
from django.db import models
User = get_user_model()


def get_percentage(amount,percentage):
    return (percentage / 100) *amount

class CartItem(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product         = models.ForeignKey(Product, on_delete=models.CASCADE)

    ordered         = models.BooleanField(default=False)

    quantity        = models.IntegerField(default=1)

    created_at      = models.DateTimeField(auto_now_add=True)

    sub_attributes  = models.ManyToManyField('product.SAttribute',blank=True)

    @property
    def get_price(self):
        return float(self.product.price) * float(self.quantity) 

    @property 
    def coupon_code(self):
        from product.models import CouponCode
        coupon_objects = CouponCode.objects.all() 
        for i in coupon_objects:
            if self in i.cart_items.all():
                True
                break
        return False 

class Order(models.Model):
    CHOICES  =  (
        ("ship", "ship"),
        ("pickup", "pickup"),
    )
    email                   = models.EmailField(blank=True, null=True)

    user                    = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True)
    coupon_code             = models.ForeignKey('product.CouponCode',on_delete=models.CASCADE,blank=True, null=True)

    ref_code                = models.CharField(max_length=20, blank=True, null=True)
    delivery_methods        = models.CharField(choices=CHOICES,max_length=20,blank=True, null=True)

    items                   = models.ManyToManyField(CartItem)
    
    start_date              = models.DateTimeField(auto_now_add=True)
    ordered_date            = models.DateTimeField(blank=True, null=True)

    ordered                 = models.BooleanField(default=False,blank=True, null=True)
    shipping                = models.BooleanField(default=False,blank=True, null=True)
    being_delivered         = models.BooleanField(default=False,blank=True, null=True)
    received                = models.BooleanField(default=False,blank=True, null=True)
    refund_requested        = models.BooleanField(default=False,blank=True, null=True)
    refund_granted          = models.BooleanField(default=False,blank=True, null=True)
    order_cancalled         = models.BooleanField(default=False,blank=True, null=True) 
    being_delivered         = models.BooleanField(default=False,blank=True, null=True)
    received                = models.BooleanField(default=False,blank=True, null=True)


    def __str__(self):
        return str(self.id)
    
    @property
    def total_price_wo_tax(self):
        total = 0.0
        items = self.items.all()
        for price in items:
            total += price.get_price

        return float(total)


    @property
    def total_price_w_tax(self):
        total = 0
        items = self.items.all()
        for price in items:
            total += price.get_price
        
        total_orginal = total
        # check if coupon code exist
        if self.coupon_code :
            discount = get_percentage(self.coupon_code.percentage , total)
            total = total -discount

        # adding tax 
        tax_amount = total_orginal * 0.05
        total = total + tax_amount 
        return total

    @property
    def total_price_w_tax_order_overview(self):    
        #checking method for shipping
        if self.delivery_methods == 'ship':
            return '{0:.3g}'.format(self.total_price_w_tax + 20.0)
        else:
            return '{0:.3g}'.format(self.total_price_w_tax)

    @property
    def total_price_wo_tax_order_overview(self):
        #checking method for shipping
        if self.delivery_methods == 'ship':
            return '{0:.3g}'.format(self.total_price_wo_tax + 20.0)
        else:
            return '{0:.3g}'.format(self.total_price_wo_tax)
    
    @property
    def tax(self):
        total = 0
        items = self.items.all()
        for price in items:
            total += price.get_price        
        tax_amount = total * 0.05
        return '{0:.3g}'.format(tax_amount)

    @property
    def coupon_discount(self):

        #check if coupon_code exist or not
        if self.coupon_code == None:
            return False

        total = 0
        items = self.items.all()

        # calculate total amount
        for price in items:
            total += price.get_price
        coupon_discount_amount = get_percentage(self.coupon_code.percentage , total)
        return coupon_discount_amount


        
class BillingAddress(models.Model):
    
    first_name   = models.CharField(max_length=100)
    last_name    = models.CharField(max_length=100)
    address      = models.CharField(max_length=200)
    state        = models.CharField(max_length=200)
    country      = models.CharField(max_length=200)
    city         = models.CharField(max_length=200)
    phone        = models.CharField(max_length=200)
    order        = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True,null=True) 
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class ShippingAddress(models.Model):
   
    first_name   = models.CharField(max_length=100)
    last_name    = models.CharField(max_length=100)
    address      = models.CharField(max_length=200)
    state        = models.CharField(max_length=200)
    country      = models.CharField(max_length=200)
    city         = models.CharField(max_length=200)
    phone        = models.CharField(max_length=200)
    order        = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True,null=True) 
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

