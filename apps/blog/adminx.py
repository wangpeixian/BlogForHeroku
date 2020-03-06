import extra_apps.xadmin
from extra_apps import xadmin

from .models import *


class ArticleAdmin(object):
    # 展示字段
    list_display = ["id", "title", "create_time", "category", "status"]
    # 搜索关键字
    search_fields = ["title"]
    # 筛选条件
    list_filter = ["title", "create_time", "category", "status"]
    # 默认排序
    ordering = ["-id"]


class ArticleCategoryAdmin(object):
    list_display = ["id", "name"]
    search_fields = ["name"]


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(ArticleCategory, ArticleCategoryAdmin)
