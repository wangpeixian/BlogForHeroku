from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from apps.book.models import Book
from apps.movie.models import MovieCategory
from mysite.settings import BOOK_MOVIE_PAGINATE_BY


# Create your views here.

# 影书书单页父类
class MovieBookListView(ListView):
    template_name = 'book/books.html' # 跳转到 books.html 中
    context_object_name = 'lists' # 在 books.html 使用 lists 表示传递过去的内容
    paginate_by = BOOK_MOVIE_PAGINATE_BY # 每页显示的数量

    # 准备传递的内容
    def get_queryset(self):
        return Book.objects.all()


# 某标签下的书籍列表
class BookListView(MovieBookListView):
    template_name = 'book/book_list.html'

    def get_queryset(self):
        tag = get_object_or_404(MovieCategory, pk=self.kwargs.get('pk')) # url匹配的参数传递给pk
        self.tag_name = tag.name
        return Book.objects.filter(tag=tag)

    def get_context_data(self, **kwargs):
        kwargs['tag_name'] = self.tag_name
        return super(BookListView, self).get_context_data(**kwargs)