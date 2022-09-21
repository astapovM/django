from django.shortcuts import render

from django.http import HttpResponse
from .models import Blog, Category


def index(request):
    blog = Blog.objects.all()
    categories = Category.objects.all()
    context = {
        'blog': blog,
        'title': 'Список событий',
        'categories': categories,
    }

    return render(request, 'blog/index2.html', context=context)

def get_category(request, category_id):
    blog = Blog.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'blog/category.html', {"blog": blog, "categories": categories, "category": category})
