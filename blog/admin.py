from django.contrib import admin
from .models import Blog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'is_published']
    list_display_links = ['title']
    search_fields = ['title', 'content']

admin.site.register(Blog,BlogAdmin)