from django.urls import path

from blog.views import *

urlpatterns = [
    path('', HomeBlog.as_view(), name='home'),
    path('category_<int:category_id>/', BlogByCategory.as_view(extra_context={'title':'Какой-то тайтл'}), name='category'),
    # path('blog/<int:blog_id>/', view_blog, name='view_blog'),
    path('blog/<int:pk>/', ViewBlog.as_view(), name='view_blog'),
    path('blog/add-blog/', add_blog, name="add_blog"),
    path('api/v1/bloglist', BlogApiList.as_view()),
    path('api/v1/bloglist/<int:pk>/', BlogApiList.as_view()),
]