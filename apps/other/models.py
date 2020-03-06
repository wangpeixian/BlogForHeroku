from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class MeanList(models.Model):
    """
    菜单栏
    """

    STATUS = (
        ('y', '显示'),
        ('n', '隐藏'),
    )

    title = models.CharField("菜单名称", max_length=100)
    link = models.CharField("菜单链接", max_length=100, blank=True, null=True, )
    icon = models.CharField("菜单图标", max_length=100, blank=True, null=True, )
    status = models.CharField('显示状态', max_length=1, choices=STATUS, default='y')

    class Meta:
        verbose_name = "菜单栏"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    """
    评论
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name="评论来源")
    object_id = models.PositiveIntegerField("评论对象")
    content_object = GenericForeignKey('content_type', 'object_id')

    text = RichTextField("评论内容")
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="评论用户")

    root = models.ForeignKey('self', related_name='root_comment', null=True, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='parent_comment', null=True, on_delete=models.CASCADE)
    reply_to = models.ForeignKey(User, related_name='replies', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "我的评论"
        verbose_name_plural = verbose_name
        ordering = ['-comment_time']


# 友情链接
class FriendLinks(models.Model):
    name = models.CharField('网站名称', max_length=50, default="")
    link = models.CharField('网站地址', max_length=200, default="")

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name
        ordering = ['-pk']


# 社交账号
class Social(models.Model):
    github = models.URLField(verbose_name="Github", max_length=200, default='https://github.com/wangpeixian')
    wechat = models.CharField(verbose_name="微信", max_length=50, default="")
    email = models.CharField(verbose_name="邮箱", max_length=50, default="")

    class Meta:
        verbose_name = "联系方式"
        verbose_name_plural = verbose_name
