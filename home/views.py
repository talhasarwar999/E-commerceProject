from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.shortcuts import render
from product.models import *

from functools import wraps
from home.models import *
from utils import *




def home(request):
    home_page_contents = HomePageContent.objects.filter().first()
    home_page_sliders = HomePageSlider.objects.all()
    products = Product.objects.filter()
    grand_categories = GrandCategory.objects.filter()
    parent_categories = ParentCategory.objects.filter()
    child_categories = ChildCategory.objects.filter()

    context = {}
    print(request.user)
    print(request.user.is_authenticated)
    if request.user.is_authenticated == True:   
        print('coming here')
        carItem = CartItem.objects.filter(
            user=request.user
            ) 
        context['carItem']            = carItem
        
    context['home_page_contents'] = home_page_contents
    context['home_page_sliders']  = home_page_sliders
    context['categories']         = grand_categories
    context['parent_categories']  = parent_categories
    context['child_categories']   = child_categories
    context['products']           = products

    return render(request,'home.html',context)

    


class FAQView(TemplateView):
    template_name = "faq.html"
    
class PrivacyPolicyView(TemplateView):
    template_name = "privacy_policy.html"
    
    
class TermsConditionView(TemplateView):
    template_name = "terms_and_conditions.html"
