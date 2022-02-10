from django.shortcuts import redirect, render
from contact.form import *
from utils import *


def ContactUs(request):
    context = {}

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        print('contact_form_error:', contact_form.errors)
        print('imm in post')
        if contact_form.is_valid():
            obj = contact_form.save()
            obj.save()
            print('Form Saved')
            sendEmailContact(obj,'',request) 
        else:
            return redirect('contact-us')

    contact_form = ContactForm(request.POST, prefix='contact_form')

    context['form'] = ContactForm()
    return render(request, 'contact_us.html', context=context)
