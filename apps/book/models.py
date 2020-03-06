from django.db import models

# Create your models here.
from django.utils import timezone


class BookCategory(models.Model):
    """
    图书分类名称
    """
    name = models.CharField(verbose_name="图书分类", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "图书分类"
        verbose_name_plural = verbose_name


class Book(models.Model):
    """
    图书信息
    """
    name = models.CharField(verbose_name="书名", max_length=100)
    author = models.CharField(verbose_name="作者", max_length=100)
    # category = models.ForeignKey
    image = models.ImageField(verbose_name="封面图", upload_to="images/books", blank=True)
    score = models.DecimalField(verbose_name="评分", max_digits=2, decimal_places=1)  # 最大长度为两位(两个数字), 最多有一个小数位
    create_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "图书信息"
        verbose_name_plural = verbose_name
