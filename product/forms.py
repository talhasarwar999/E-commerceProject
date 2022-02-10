from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = (
         'title',
         'code',
         'price',
         'thumbnail',
         'is_active',
         'sub_title',
         'sold_times',
         'is_featured',
         'is_bestSeller',
        #  'grand_category',
         )    


class ProductSliderImageForm(forms.ModelForm):
        class Meta:
            model = ProductSliderImage
            fields = (
                'product',
                'image',
            )

            