from django.core.paginator import Paginator
from django.shortcuts import render
from product.models import Product


def shop(request):
    context = {}
    title = request.GET.get('title')
    if title:    
       products = Product.objects.filter(title__icontains=title)
    else:
       products = Product.objects.filter()
    
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 12)
    

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
       
    context['objects'] = products
    return render(request, 'shop.html', context=context)
 