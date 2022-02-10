from django.utils.html import format_html
from django.contrib import admin
from blog.models import *


class BlogTypeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "created_at",
    ]
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "created_at",
        "thumbnail_image",
    ]
    list_display_links = ["id"]
    readonly_fields = ["thumbnail_image"]
    def design_code(self, obj):
        return format_html('<a href="{}/update/">{}</a>'.format(obj.pk, obj.code))

    def category(self, obj):
        return obj.category.category_name

    def thumbnail_image(self, obj):
        try:                 
            return format_html(
                '<img src="{}" style="max-width: 200px;"/>'.format(obj.thumbnail.url)
            )
        except:
            return '' 

    thumbnail_image.allow_tags = True
    thumbnail_image.short_description = "thumbnail preview"


admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogType,BlogTypeAdmin)

