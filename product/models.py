from django.db.models.enums import Choices
from django.template.defaultfilters import default, slugify
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.db import models
from home.models import *


User = get_user_model()


# ----------------------------------------------------------------------#
# ---------------------------- Category --------------------------------#
# ----------------------------------------------------------------------#
class GrandCategory(models.Model):
    name = models.CharField(max_length=1000)
    icon = models.ImageField(upload_to="media/grand_category/thumbnail", null=True, blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name

    @property
    def get_products(self):
        from product.models import Product
        return Product.objects.filter(grand_category = self)

    @property
    def get_attributes(self):
        from product.models import Attribute
        return Attribute.objects.filter(grand_category=self)

    class Meta:
        verbose_name_plural = "Grand Categories"

class Box(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="media/box/icon", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name  

class ParentCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="media/parent_category/icon", null=True, blank=True)
    grand_category = models.ForeignKey(GrandCategory, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def get_child_categories(self):
        from product.models import ChildCategory
        return ChildCategory.objects.filter(parent_category=self)

    class Meta:
        verbose_name_plural = "Parent Catagories"

class ChildCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="media/child_category/icon", null=True, blank=True)
    parent_category = models.ForeignKey(ParentCategory, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Child Catagories"

# ---------------------------- Product ---------------------------------#
# ----------------------------------------------------------------------#

class SubAttribute(models.Model):
    name = models.CharField(max_length=300, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Attribute(models.Model):
    name            = models.CharField(max_length=300, default="")
    grand_category  = models.ForeignKey(on_delete=models.CASCADE,to='product.GrandCategory')
    created_at  = models.DateTimeField(auto_now_add=True)

    @property
    def get_sub_attributes(self):
        from product.models import SAttribute
        return SAttribute.objects.filter(attribute=self)

    def __str__(self):
        return self.name
    
class SAttribute(models.Model):
    name            = models.CharField(max_length=300, default="")
    attribute       = models.ForeignKey(on_delete=models.CASCADE,to='product.Attribute')
    product         = models.ForeignKey(on_delete=models.CASCADE,to='product.Product',default=5,blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    slug            = models.SlugField(unique=True)
    grand_category  = models.ForeignKey(GrandCategory, on_delete=models.CASCADE,blank=True,null=True)
    parent_category = models.ForeignKey(ParentCategory, on_delete=models.CASCADE,blank=True,null=True)
    child_category  = models.ForeignKey(ChildCategory, on_delete=models.CASCADE,blank=True,null=True)

    sub_attribute   = models.ManyToManyField(SubAttribute, related_name='sub_property',blank=True)
    box             = models.ManyToManyField('product.Box',blank=True)


    description     = models.TextField()

    code            = models.CharField(max_length=50, default="")
    title           = models.CharField(max_length=50, default="")
    sub_title       = models.CharField(max_length=50, default="")

    price           = models.FloatField(default=0.0)
    sold_times      = models.IntegerField(default=0, null=True, blank=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    thumbnail       = models.ImageField(upload_to="media/product/thumbnail", default="", blank=True)

    is_active       = models.BooleanField(default=False)
    is_featured     = models.BooleanField(default=False)
    is_bestSeller   = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

    @property
    def get_attributes(self):
        from product.models import Attribute,ProductSliderImage
        slider_image = ProductSliderImage.objects.filter(product=self).values('attribute')
        slider_image_id_list = list(set([i['attribute'] for i in slider_image]))
        return Attribute.objects.filter(id__in=slider_image_id_list)

    @property
    def get_sub_attributes(self):
        from product.models import SubAttribute,ProductSliderImage
        slider_image = ProductSliderImage.objects.filter(product=self).values('sub_attribute')
        slider_image_id_list = list(set([i['sub_attribute'] for i in slider_image]))
        return SubAttribute.objects.filter(id__in=slider_image_id_list)

class ProductSliderImage(models.Model):
    product = models.ForeignKey( 
        Product,
        on_delete=models.CASCADE,
        related_name="product_slider_images",
        null=True,
        blank=True, )
    image = models.ImageField(upload_to="media/productSliderImage/image")
    created_at = models.DateTimeField(auto_now_add=True)

    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, null=True)
    sub_attribute = models.ForeignKey(SAttribute, on_delete=models.CASCADE, null=True)
    related_sub_attribute = models.ForeignKey(SAttribute, on_delete=models.CASCADE, null=True,related_name='related_sub_attribute')


    def __str__(self):
        return str(self.id)

    @property
    def get_attributes(self):
        from product.models import Attribute
        return Attribute.objects.filter(id=self.attribute.id)
    @property
    def get_sub_attribute(self):
        from product.models import SubAttribute
        return SubAttribute.objects.filter(id=self.attribute.id)

class CouponCode(models.Model):
    code            = models.CharField(max_length=10,blank=True,null=True)
    percentage      = models.FloatField()
    created_at      = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.code

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_product_receiver, sender=Product)


def create_slug_for_category(instance, new_slug=None):
    slug = slugify(instance.name)  
    if new_slug is not None:
        slug = new_slug
    qs = GrandCategory.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_category_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_for_category(instance)


pre_save.connect(pre_save_category_receiver, sender=GrandCategory)
pre_save.connect(pre_save_product_receiver, sender=Product)



def random_char(y):
    import random
    return ''.join(random.choice('ABCDEFGHIJKLNOPQRSTUVXYZ0123456789') for x in range(y))


def pre_save_coupon_code(sender, instance, *args, **kwargs):
    if not CouponCode.objects.filter(id=instance.id).exists():
        instance.code = random_char(6)



pre_save.connect(pre_save_coupon_code, sender=CouponCode)

