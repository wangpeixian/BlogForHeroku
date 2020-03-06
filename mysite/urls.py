"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from extra_apps import xadmin
from mysite import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', xadmin.site.urls, name="admin"),

    # 博客
    path("", include('apps.blog.urls')),

    # 图书
    path("", include("apps.book.urls")),

    # 电影
    path("", include("apps.movie.urls")),

    # 用户
    path("", include("apps.user.urls")),

    # 其他
    path("", include("apps.other.urls")),

    # 消息通知模块
    path('notifications/', include('notifications.urls', namespace='notifications')),

    # 搜索模块
    path('search/', include('haystack.urls')),

    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),  # 上传的文件
]
