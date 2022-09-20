from django.shortcuts import render

from django.http import HttpResponse
from .models import Blog

def index(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog,
        'title': 'Список событий'
    }
    return render(request, 'blog/index.html', context)



