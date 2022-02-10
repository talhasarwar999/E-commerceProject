from django.contrib.auth import get_user_model
from django.contrib import admin
from accounts.models import *

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','is_active','is_staff','is_superuser','date_joined',) 

admin.site.register(User,UserAdmin)


