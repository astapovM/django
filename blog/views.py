from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .forms import BlogForm
from .models import Blog, Category
from .serializers import BlogSerializer


class HomeBlog(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogByCategory(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewBlog(DetailView):
    model = Blog
    context_object_name = 'blog_item'


def view_blog(request, blog_id):
    # blog_item = Blog.objects.get(pk=blog_id)
    blog_item = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/view_blog.html', {'blog_item': blog_item})


def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            Blog.objects.create(**form.cleaned_data)
            return redirect("home")
    else:
        form = BlogForm()
    return render(request, 'blog/add_blog.html', {'form': form})


class BlogApiList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogUpdateList(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class BlogApiDestroy(generics.RetrieveDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


# class BlogViewSet(viewsets.ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer