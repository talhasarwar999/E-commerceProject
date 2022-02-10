
from django.utils.html import format_html
from django.contrib import admin
from product.models import *
from home.models import *


class ProductSliderImageAdmin(admin.StackedInline):  
    model =  ProductSliderImage
    extra =  1

class ProductAdmin(admin.ModelAdmin):
       
    list_display = ("id", "product_title", "price", "description", "created_at", "updated_at","view_image_in_admin",)
    readonly_fields = ("view_image_in_admin",)


    list_display_links = ["product_title"]

    def product_title(self,obj):
        return format_html('<a href="/product/admin/{}/">{}</a>'.format(obj.pk, obj.title))
    
    def view_image_in_admin(self, obj):
        try:
            return format_html(
                '<img src="{}" style="width: 200px; height: 150px;"/>'.format(obj.thumbnail.url)
            )
        except:
            return ''
        
    view_image_in_admin.short_description = "Image"
    inlines = [ProductSliderImageAdmin]
    exclude = ('slug',) 
    
    product_title.short_description = "title"
    product_title.allow_tags = True
    
    class Media:
            js = ("assets/js/product.js",) 

class AttributeAdmin(admin.StackedInline):  
    model =  Attribute
    extra =  1

class GrandCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "created_at",
        "icon_display",
    ]
    list_display_links = ["id"]
    readonly_fields = ["icon_display"]
    exclude = ('slug',)  
    inlines = [AttributeAdmin,]
    def design_code(self, obj):
        return format_html('<a href="{}/update/">{}</a>'.format(obj.pk, obj.code))

    def icon_display(self, obj):
        try:
            return format_html(
                '<img src="{}" style="width: 200px; height: 150px;"/>'.format(obj.icon.url)
            )
        except:
            return ''

    icon_display.allow_tags = True
    icon_display.short_description = "Icon Preview"  

class ChildCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "created_at",
        "icon_display",
    ]
    list_display_links = ["id"]
    readonly_fields = ["icon_display"]

    def design_code(self, obj):
        return format_html('<a href="{}/update/">{}</a>'.format(obj.pk, obj.code))

    def icon_display(self, obj):
        try:
            return format_html(
                '<img src="{}" style="width: 200px; height: 150px;"/>'.format(obj.icon.url)
            )
        except:
            return ''

    icon_display.allow_tags = True
    icon_display.short_description = "Icon Preview"  

class ChildCategoryAdmin(admin.StackedInline):  
    model =  ChildCategory
    extra =  1

class ParentCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "created_at",
        "icon_display",
    ]
    list_display_links = ["id"]
    readonly_fields = ["icon_display"]
    inlines = [ChildCategoryAdmin]

    def design_code(self, obj):
        return format_html('<a href="{}/update/">{}</a>'.format(obj.pk, obj.code))

    def icon_display(self, obj):
        try:
            return format_html(
                '<img src="{}" style="width: 200px; height: 150px;"/>'.format(obj.icon.url)
            )
        except:
            return ''

    icon_display.allow_tags = True
    icon_display.short_description = "Icon Preview"  


class AttributeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "created_at",
    ]
    list_display_links = ["id"]

class SubAttributeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "created_at",
    ]
    list_display_links = ["id"]

class CouponCodeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "code",
        "percentage",
        "created_at",
    ]    
    exclude = ['code'] 
    readonly_fields = ('code',)  


class BoxAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "created_at",
        'icon_display',

    ]    

    def icon_display(self, obj):
        try:
            return format_html(
                '<img src="{}" style="width: 200px; height: 150px;"/>'.format(obj.icon.url)
            )
        except:
            return ''

    icon_display.allow_tags = True
    icon_display.short_description = "Icon Preview"  

admin.site.register(GrandCategory,GrandCategoryAdmin)
admin.site.register(ParentCategory,ParentCategoryAdmin) 
admin.site.register(SubAttribute,SubAttributeAdmin)
admin.site.register(CouponCode, CouponCodeAdmin)
admin.site.register(Attribute,AttributeAdmin)  
admin.site.register(Product, ProductAdmin)
admin.site.register(Box,BoxAdmin)
admin.site.register(SAttribute)
admin.site.register(ProductSliderImage)  




