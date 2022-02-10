from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.db import models
User = get_user_model()



class BlogType(models.Model):
    title       = models.CharField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title       = models.CharField(max_length=200)
    thumbnail   = models.ImageField(upload_to="media/blog/thumbnail", null=True, blank=True)
    user        = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    blog_type   = models.ForeignKey(BlogType, null=True, on_delete=models.SET_NULL)
    description = RichTextField()
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

