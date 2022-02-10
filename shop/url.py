from django.urls import path, include
from shop.views import *

urlpatterns = [
    path('shop/', shop, name='shop')
]
