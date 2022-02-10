from django.contrib import admin

# Register your models here.
from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'contacted_on')

    class Meta:
        verbose_name = "Contact Page"


admin.site.register(Contact, ContactAdmin)
