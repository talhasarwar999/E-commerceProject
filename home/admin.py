from django.utils.html import format_html
from django.contrib import admin
from home.models import *
from utils import AdminImageWidget


class NavLinksAdmin(admin.StackedInline):
    extra = 1
    max_num = 4
    model = NavLink
    list_display = [
        "id",
        "nav_title", 
    ]
    list_display_links = ["id"]

    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

class FooterAdmin(admin.StackedInline):
    extra = 1
    max_num = 1
    model = Footer
    list_display_links = ["id"]

    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

class HeaderAdmin(admin.StackedInline):
    extra = 1
    max_num = 1
    model = Header
    list_display_links = ["id"]

    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}



class HomePageSliderAdmin(admin.StackedInline):
    extra = 1
    model = HomePageSlider
    list_display = [
        "id",
    ]
    list_display_links = ["id"]
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

class HomePageContentAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "bestseller_product_title",
        "logo_preview",

    ]
    list_display_links = ["id"]
    readonly_fields = ["logo_preview"]
    inlines  = [HeaderAdmin,NavLinksAdmin,HomePageSliderAdmin,FooterAdmin]

    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

    def logo_preview(self, obj):
        try:                 
            return format_html(
                '<img src="{}" style="max-width: 200px;"/>'.format(obj.logo.url)
            )
        except:
            return '' 

    logo_preview.allow_tags = True
    logo_preview.short_description = "logo preview"

    def add_view(self, request, form_url='', extra_context=None):
        obj = HomePageContent.objects.all().first()  
        if obj:
            return self.change_view(request, object_id=str(obj.id) if obj else None)
        else:
            return super(type(self), self).add_view(request, form_url, extra_context)

    def changelist_view(self, request, extra_context=None):
        return self.add_view(request)
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save_and_add_another': False,
            'show_save_and_continue': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
       

    class Media:
        js = (
            'assets/js/script.js',  
            )
            

admin.site.register(HomePageContent,HomePageContentAdmin)

