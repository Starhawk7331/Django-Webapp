from django.contrib import admin
from .models import cat_pic, post_image

class PostImageAdmin(admin.StackedInline):
    model = post_image

@admin.register(cat_pic)
class cat_picsAdmin(admin.ModelAdmin):
    list_display = ["title","image"]

@admin.register(post_image)
class Post_ImageAdmin(admin.ModelAdmin):
    pass