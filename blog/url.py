from django import urls
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from blog.views import *

urlpatterns = [
    path('blogs/',blog_list,name='blog-list'),
    path('blog/<id>/',blog_detail,name='blog-detail'),
]