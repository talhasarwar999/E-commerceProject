from django.template import Library
from django.db.models import Sum

register = Library()
@register.filter
def running_total(role_total):
     print('***************************')
     print(role_total)
     rzlt = sum([i.get_price for i in role_total] )
     print(rzlt) 
     print('***************************')


     return rzlt
     