from django.db import models

class cat_pics(models.Model):
    
    title = models.CharField(max_length=30,default='')
    image = models.ImageField(upload_to='test_website/images/cats',default='')