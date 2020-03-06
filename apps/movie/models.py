from django.db import models


class MovieCategory(models.Model):
    """
    电影分类
    """
    name = models.CharField(verbose_name="电影分类", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "电影分类"
        verbose_name_plural = verbose_name


class Movie(models.Model):
    """
    电影
    """
    name = models.CharField(verbose_name="电影名称", max_length=100)
    director = models.CharField(verbose_name="导演", max_length=100)
    # actor = models.ForeignKey()
    # category = models.ForeignKey()
    image = models.ImageField(verbose_name="封面图", upload_to="image/movie", blank=True)
    score = models.DecimalField(verbose_name="评分", max_digits=2, decimal_places=1)
    release_time = models.DateField(verbose_name="上映时间")
    length_time = models.PositiveIntegerField(verbose_name="电影时长", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "电影"
        verbose_name_plural = verbose_name
