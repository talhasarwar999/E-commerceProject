from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from contact.views import *

urlpatterns = [
    path('ContactUs/', ContactUs,name='contact-us')
]
