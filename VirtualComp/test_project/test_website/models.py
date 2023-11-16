from django.db import models
from . import forms

class cat_pic(models.Model):
    
    title = models.CharField(max_length=100,default='')
    image = forms.ImageFieldForm()
    #image = models.ImageField()
    models.FilePathField.recursive = True
    models.FilePathField.allow_folders = True