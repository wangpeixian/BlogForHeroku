from django.urls import path

from . import views

app_name = 'movie'
urlpatterns = [
    path('movies/', views.MoviesView.as_view(), name='movies'), # 电影列表

    path('movie_list/<int:pk>', views.MovieListView.as_view(), name='movie_list'), # 某分类下的电影列表
]