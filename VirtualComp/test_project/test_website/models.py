from django.db import models

class cat_pic(models.Model):
    
    title = models.CharField(max_length=100,default='')
    image = models.ImageField(upload_to='test_website/images/cats' + str(title),default='')
    models.FilePathField.recursive = True
    models.FilePathField.allow_folders = True