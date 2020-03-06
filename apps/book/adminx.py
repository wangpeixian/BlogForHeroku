from extra_apps import xadmin

from .models import *


class BookAdmin(object):
    # 展示字段
    list_display = ["id", "name", "author", "score"]
    # 搜索关键字
    search_fields = ["name"]
    # 筛选条件
    list_filter = ["name", "author", "score"]
    # 默认排序
    ordering = ["-id"]


class BookCategoryAdmin(object):
    # 展示字段
    list_display = ['id', 'name']
    search_fields = ['name']


xadmin.site.register(Book, BookAdmin)
xadmin.site.register(BookCategory, BookCategoryAdmin)
