from django.urls import path

from apps.blog.views import article, ArticleIndex, Categories, CategoryView
from . import views

app_name = 'blog'
urlpatterns = [
    path('', ArticleIndex.as_view(), name='index'), # 博客主页

    path('categories/', Categories.as_view(), name='categories'), # 博客文章分类列表页

    path('category/<int:pk>', CategoryView.as_view(), name='category'), # 某一分类下的文章

    path('article/<int:pk>', article, name='article'), # 文章详情


]