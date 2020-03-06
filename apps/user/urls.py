from django.contrib import admin
from django.urls import path, include

from apps.user.views import login, register
from extra_apps import xadmin

app_name = "user"

urlpatterns = [
    path('login/', login, name="login"), # 登陆

    path('register/', register, name='register'), # 注册
]