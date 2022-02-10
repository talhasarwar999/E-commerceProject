from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=1000)
    contacted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

