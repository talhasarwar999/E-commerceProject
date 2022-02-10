from django.forms import ModelForm
from contact.models import Contact
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'phone_number',
            'email',
            'subject',
            'message',
                ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email'


