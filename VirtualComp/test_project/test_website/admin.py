from django.contrib import admin
from .models import cat_pic

class cat_picsAdmin(admin.ModelAdmin):
    list_display = ["title","image"]

admin.site.register(cat_pic, cat_picsAdmin)
