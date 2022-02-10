
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from order.views import *

urlpatterns = [
    path('addToCart/',addToCart,name='add-to-cart'),
    path('cart/',cart_list,name='cart-list'),
    path('changeQuantity/',changeQuantity,name='change-quantity'),
    path('removeToCart/',removeToCart,name='remove-to-cart'),
    path('payment/',orderView,name='payment-detail'),  
    path('coupon/',applyCoupon,name='apply-coupon'),  
    path('order/thankyou/',thankYou,name='thank-you'),

] 

