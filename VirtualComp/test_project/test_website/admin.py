from django.contrib import admin
from .models import cat_pic


@admin.register(cat_pic)
class cat_picsAdmin(admin.ModelAdmin):
    list_display = ["title","description","get_likes","get_images"]

    def get_likes(self, obj):
        return "\n".join([p.likes for p in obj.likes.all()])
    
    def get_images(self, obj):
        return "\n".join([p.image for p in obj.image.all()])

