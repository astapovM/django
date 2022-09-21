from django.urls import path

from blog.views import *

urlpatterns = [
    path('', index, name='home'),
    path('category_<int:category_id>/', get_category, name='category')

]