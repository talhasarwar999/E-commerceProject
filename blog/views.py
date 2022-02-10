from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect
from django.contrib import messages
from blog.models import *
from blog.forms import *
from utils import *

def blog_list(request):
    objects_list = Blog.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(objects_list, 9)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)    
    context = {}
    context['objects'] = objects
    return render(request,'blog_list.html',context)

def blog_detail(request,id):
    try:
        Blog.objects.get(id=id)
    except:
        messages.warning(request, 'Blog not found.')
        return redirect('blog-list')

    object = Blog.objects.get(id=id)

    context = {}
    context['object'] = object
    return render(request,'blog_detail.html',context)

