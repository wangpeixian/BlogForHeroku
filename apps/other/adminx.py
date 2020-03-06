from extra_apps import xadmin
from .models import *


class FriendLinksAdmin(object):
    list_display = ['id', 'name', 'link']
    model_icon = 'fa fa-link'


class SocialAdmin(object):
    list_display = ['id', 'github', 'wechat', "email"]
    model_icon = 'fa fa-weibo'


xadmin.site.register(FriendLinks, FriendLinksAdmin)
xadmin.site.register(Social, SocialAdmin)
