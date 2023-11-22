from django.db import models
from . import forms



class post_image(models.Model):
    images = models.ImageField(default=None,upload_to='test_website/images/cats/%Y-%m/%Y-%m-%d')

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class cat_pic(models.Model):

    title = models.CharField(max_length=100,default='')
    description = models.TextField(default=None)
    image = models.ForeignKey(post_image,default=None,on_delete=models.CASCADE)
    dates = models.ForeignKey(TimeStampMixin,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    