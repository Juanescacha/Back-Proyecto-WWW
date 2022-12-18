from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "descripcion", "url_media", "estado")


admin.site.register(Post, PostAdmin)
