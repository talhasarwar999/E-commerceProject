from django import forms
from django.forms import ModelForm
from order.models import *
from django import forms

# class PaymentForm(ModelForm):
#     class Meta:
#         model = Payment
#         fields = [
#             'email',
#             'delivery_methods',
#             # 'shipping_address',
#                 ]
#         widgets = {
#         'delivery_methods': forms.RadioSelect(),
#         }                   
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['email'].widget.attrs['placeholder'] = 'Email'

class ShippingAddressForm(ModelForm):
    class Meta:
         model =  ShippingAddress
         fields = ['first_name',
                   'last_name',
                   'address',
                   'country',
                   'phone',
                   'state',
                   'city',
                   ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']    = 'First Name '
        self.fields['last_name'].widget.attrs['placeholder']     = 'Last Name '
        self.fields['address'].widget.attrs['placeholder']       = 'Address'
        self.fields['country'].widget.attrs['placeholder']       = 'Country'
        self.fields['country'].widget.attrs['class']             = 'country'
        self.fields['city'].widget.attrs['class']                = 'cities'
        self.fields['state'].widget.attrs['class']               = 'states'
        self.fields['phone'].widget.attrs['placeholder']         = 'Phone'
        self.fields['state'].widget.attrs['placeholder']         = 'state'

        # self.fields['title'].widget.attrs['id'] = 'title-career'
        # self.fields['description'].widget.attrs['class'] = 'form-control'
        # self.fields['postType'].widget.attrs['class'] = 'form-control'
        # self.fields['image'].widget.attrs['class'] = 'file-path validate'
        # self.fields['image'].required = False

class BillingAddressForm(ModelForm):
    class Meta:
         model =  BillingAddress
         fields = ['first_name',
                   'last_name',
                   'address',
                   'country',
                   'phone',
                   'state',
                   'city',
                   ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']    = 'First Name '
        self.fields['last_name'].widget.attrs['placeholder']     = 'Last Name '
        self.fields['address'].widget.attrs['placeholder']       = 'Address'
        self.fields['country'].widget.attrs['placeholder']       = 'Country'
        self.fields['country'].widget.attrs['class']             = 'country'
        self.fields['city'].widget.attrs['class']                = 'cities'
        self.fields['state'].widget.attrs['class']               = 'states'
        self.fields['phone'].widget.attrs['placeholder']         = 'Phone'
        self.fields['state'].widget.attrs['placeholder']         = 'state'





