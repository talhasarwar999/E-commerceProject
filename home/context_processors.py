
from home.models import NavLink,Footer,Header
from product.models import GrandCategory
from order.models import CartItem


def get_links(request): 
    nav_links = NavLink.objects.filter() 
    footer = Footer.objects.filter().first()
    header = Header.objects.filter().first()
    categories = GrandCategory.objects.filter()
    context = {}
    
    if request.user.is_authenticated:
        cartItem = CartItem.objects.filter(user=request.user)  
        context['cartItem'] = cartItem
        
    context['nav_links'] = nav_links
    context['categories'] = categories
    context['footer'] = footer
    context['header'] = header
    return  context
 

 