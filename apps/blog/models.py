from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

from django.db import models


class ArticleCategory(models.Model):
    """
    文章所属分类
    """
    name = models.CharField("分类名称", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'pk': self.pk})


class Article(models.Model):
    """
    博客文章
    """

    STATUS = (
        ("y", "置顶"),
        ("n", "不置顶"),
    )

    title = models.CharField(verbose_name="标题", max_length=100, unique=True)
    body = models.TextField(verbose_name="正文")
    create_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)  # 默认时间为当前时间
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)  # 每次修改时自动更改时间
    summary = models.CharField(verbose_name="摘要", max_length=200, blank=True)
    views = models.IntegerField(verbose_name="阅读人数", default=0)
    words = models.IntegerField(verbose_name="字数", default=0)
    category = models.ForeignKey(ArticleCategory, verbose_name="文章所属分类", on_delete=models.CASCADE)  # 文章所属分类
    author = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)  # 文章所属作者
    status = models.CharField("是否置顶", choices=STATUS, default="n", max_length=2)  # 默认为不置顶

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "博客文章信息"
        verbose_name_plural = verbose_name
        ordering = ["-create_time"]  # 根据创建时间排序

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'pk': self.pk})

    # 阅读量增加1
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
