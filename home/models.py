from django.db import models
from ckeditor.fields import RichTextField


class HomePageContent(models.Model):
    
    logo                                 = models.ImageField(upload_to="media/home/logo", null=True, blank=True)
    banner_Image                         = models.ImageField(upload_to="media/home/banner", null=True, blank=True)

    bestseller_product_title             = models.CharField(max_length=120)
    bestseller_product_title_message     = models.CharField(max_length=120)
    bestseller_product_title_description = models.CharField(max_length=120)

    featured_product_title               = models.CharField(max_length=120)
    featured_product_title_message       = models.CharField(max_length=120)
    featured_product_title_description   = models.CharField(max_length=120)



    class Meta:
        verbose_name_plural               = "Home Page Content"

class HomePageSlider(models.Model):
    slider_image        = models.ImageField(upload_to="media/home/Slider", null=True, blank=True)
    home                = models.ForeignKey(HomePageContent,on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        verbose_name_plural = "Home Page Slider"

    def __str__(self):
        return str(self.id)
        
class NavLink(models.Model): 
    nav_title  = models.CharField(max_length=1000)
    category   = models.OneToOneField(to="product.GrandCategory",on_delete=models.CASCADE)
    home        = models.ForeignKey(HomePageContent,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return str(self.id)
 
class Footer(models.Model):
    footer_title    = models.CharField(max_length=1000)
    facebook_link   = models.URLField(blank=True)
    twitter_link    = models.URLField(blank=True)
    instagram_link  = models.URLField(blank=True)
    linkedin_link   = models.URLField(blank=True)
    office_address  = models.CharField(max_length=2000)
    phone_no        = models.CharField(max_length=1000)
    email           = models.EmailField()
    home            = models.ForeignKey(HomePageContent,on_delete=models.CASCADE,blank=True)
 
    def __str__(self):
        return str(self.id)

class Header(models.Model):
    phone_no        = models.CharField(max_length=1000)
    email           = models.EmailField()
    home            = models.ForeignKey(HomePageContent,on_delete=models.CASCADE,blank=True)
 
    def __str__(self):
        return str(self.id)

