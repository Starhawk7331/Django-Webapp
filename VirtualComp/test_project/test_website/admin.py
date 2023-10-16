from django.contrib import admin
from .models import cat_pics

class cat_picsAdmin(admin.ModelAdmin):
    list_display = ["title","image"]

admin.site.register(cat_pics, cat_picsAdmin)
