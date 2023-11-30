from django.db import models
from django.contrib.auth.models import User

class post_image(models.Model):
    images = models.ImageField(default=None,upload_to='test_website/images/cats/%Y-%m/%Y-%m-%d')

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class LikeSystem(models.Model):
    liked_by=[]

    def like(self,User):
        if User in self.liked_by:
            self.liked_by.remove(User)
            return False
        else:
            self.liked_by.append(User)
            return True


class cat_pic(models.Model):

    title = models.CharField(max_length=100,default='')
    description = models.TextField(default=None)
    image = models.ManyToManyField(post_image,default=None)
    likes = models.ManyToManyField(LikeSystem,blank=True)

    def __str__(self):
        return self.title