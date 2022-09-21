from django.contrib import admin

from .models import Blog, Category


# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at', 'is_published']
    list_display_links = ['title']
    search_fields = ['title', 'content']
    list_editable = ['is_published']
    list_filter = ['is_published', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title', ]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
