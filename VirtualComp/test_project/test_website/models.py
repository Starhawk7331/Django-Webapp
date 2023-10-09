from django.db import models

class cat_pics(models.Model):
    path = models.TextField()
    likes = models.IntegerField