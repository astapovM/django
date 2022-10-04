from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import BlogForm
from .models import Blog, Category
from .serializers import BlogSerializer


class HomeBlog(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


# def index(request):
#     blog = Blog.objects.all()
#     categories = Category.objects.all()
#
#     context = {
#         'blog': blog,
#         'title': 'Список событий',
#         'categories': categories,
#
#     }
#     return render(request, 'blog/index2.html', context=contex

class BlogByCategory(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


# def get_category(request, category_id):
#     blog = Blog.objects.filter(category_id=category_id)
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'blog/category.html', {"blog": blog, "categories": categories, "category": category})

#
# class BlogAPIView(generics.ListAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
class BlogAPIView(APIView):
    def get(self, request):
        w = Blog.objects.all()
        return Response({'Записи': BlogSerializer(w, many=True).data})

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Blog.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            photo=request.data['photo'],
            category_id=request.data['category_id']
        )
        return Response({'post': BlogSerializer(post_new).data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
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

# def listing(request):
#     categories = Category.objects.all()
#     paginator = Paginator(categories, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'blog/index2.html', {"page_obj": page_obj})
