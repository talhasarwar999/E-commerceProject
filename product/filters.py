from  product.models import *
from  home.models import *
import django_filters


class ProductFilter(django_filters.FilterSet):
    name        = django_filters.CharFilter(lookup_expr='icontains') 

    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'created_at',
            'child_category__name',
            'child_category__parent_category',
            'child_category__parent_category',
            'child_category__parent_category__grand_category',
            ] 

