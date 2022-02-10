from django.contrib.admin.widgets import AdminFileWidget
from django.http.response import HttpResponse

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from dolce.settings import EMAIL_HOST_USER
from django.utils.html import format_html
from functools import wraps
from order.models import *
User = get_user_model()

import os



from email.mime.image import MIMEImage

from django.contrib.staticfiles import finders

def logo_data():
    with open(finders.find('assets/shirt_1.png'), 'rb') as f:
        logo_data = f.read()
    logo = MIMEImage(logo_data)
    logo.add_header('Content-ID', '<logo>')
    return logo


def sendEmail(obj,content,request):
        subject, from_email = "subject",EMAIL_HOST_USER, 
        to=obj.email
        text_content = ''
        html_content = render_to_string('email.html',{'obj':obj})
        msg = EmailMultiAlternatives(subject, text_content, from_email, [EMAIL_HOST_USER])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

def sendEmailContact(obj,content,request):
        subject, from_email = "subject",EMAIL_HOST_USER, 
        to=obj.email
        text_content = ''
        print(from_email,subject)
        html_content = render_to_string('contact_email.html',{'obj':obj})
        msg = EmailMultiAlternatives(subject, text_content, from_email, [obj.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def guest_login(function):
    @wraps(function)  # <- this is the fix!
    def wrapped(self, *args, **kwargs):
        print(self.user.is_authenticated)
        if not self.user.is_authenticated:
            ip=get_client_ip(self)
            obj , created = User.objects.get_or_create(
                ip_address=ip,
                username='___test{}'.format(ip),
                email='___test{}@gmail.com'.format(ip),
                is_staff=False,
                is_superuser=False,
                )
            login(self, obj)
        return function(self, *args, **kwargs)
    return wrapped


def check_order_confirmation(function):
    @wraps(function)  # <- this is the fix!
    def wrapped(self, *args, **kwargs):
        print(self.user.is_authenticated)
        obj = Order.objects.filter(user=self.user)
        if obj.last():
            if  obj.last().ordered:
                return HttpResponse('<h1>User not allowed!</h1>')

        return function(self, *args, **kwargs)
    return wrapped


class AdminImageWidget(AdminFileWidget):
    """Admin widget for showing clickable thumbnail of Image file fields"""

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        if value and getattr(value, 'url', None):
            html = format_html('<a href="{0}" target="_blank"><img src="{0}" alt="{1}" width="150" height="150" style="object-fit:cover;margin-bottom:30px;"/></a>', value.url, str(value)) + html
            # html = format_html('<a href="{0}" target="_blank"><img src="{0}" alt="{1}" width="150" height="150" style="object-fit:cover;margin-bottom:30px;"/></a> <br/><button id="img-delete" class="btn btn-sm btn-outline-danger mb-2"><i class="fas  fa-trash-alt"></i> </button>', value.url, str(value)) + html
        return html 


