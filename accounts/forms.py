
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
        widget = forms.EmailInput(attrs={'class':'form-control' , "placeholder":"Email Address"})
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', "class" : "form-control", "placeholder":"Password"}),
        
    )

class RegisterForm(UserCreationForm):
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
        # widget = forms.EmailInput(attrs={'class':'form-control'})
    # )
    # password1=forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    # password2=forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ['fullname','email','username','password1', 'password2']
