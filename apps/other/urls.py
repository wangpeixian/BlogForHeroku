from django.contrib import admin
from django.urls import path, include
from apps.other.views import my_notifications, delete_my_read_notifications, my_notification, update_comment

from extra_apps import xadmin

app_name = "other"

urlpatterns = [
    path('my_notifications/', my_notifications, name="my_notifications"),

    path('my_notification/<int:my_notifications_pk>', my_notification, name="my_notification"), # 将通知的序号传入, 返回该通知的链接

    path('delete_my_read_notifications', delete_my_read_notifications, name="delete_my_read_notifications"),

    path('update_comment', update_comment, name='update_comment'),
]
