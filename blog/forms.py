from django import forms  
from blog.models import *  
  
class BlogForm(forms.ModelForm):  
    class Meta:  
        model   = Blog  
        exclude = ['user',]
