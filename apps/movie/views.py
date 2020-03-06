from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
# Create your views here.

# 影单页
from apps.movie.models import Movie, MovieCategory


class MoviesView(ListView):
    template_name = 'movie/movies.html' # 跳转目标
    context_object_name = "movies" # 在前端页面的参数名称

    # 显示电影
    def get_queryset(self):
        return Movie.objects.all()

# 电影分类列表列表
class MovieListView(ListView):
    template_name = 'movie/movie_list.html'

    def get_queryset(self):
        tag = get_object_or_404(MovieCategory, pk=self.kwargs.get('pk')) # 所有的分类
        self.tag_name = tag.name
        return Movie.objects.filter(tag=tag)

    def get_context_data(self, **kwargs):
        kwargs['tag_name'] = self.tag_name # 标签列表+_+
        return super(MovieListView, self).get_context_data(**kwargs)