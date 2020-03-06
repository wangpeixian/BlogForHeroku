from extra_apps import xadmin

from .models import *


class MovieAdmin(object):
    # 展示字段
    list_display = ["id", "name", "director", "score", "length_time"]
    # 搜索关键字
    search_fields = ["name"]
    # 筛选条件
    list_filter = ["name", "author", "score"]
    # 默认排序
    ordering = ["-id"]


class MovieCategoryAdmin(object):
    # 展示字段
    list_display = ['id', 'name']
    search_fields = ['name']


xadmin.site.register(Movie, MovieAdmin)
xadmin.site.register(MovieCategory, MovieCategoryAdmin)
