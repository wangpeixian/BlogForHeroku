"""一些功能"""
from apps.blog.models import Article, ArticleCategory
from django import template
from django.db.models import Count
# from apps.comment.models import Comment
# from apps.comment.form import CommentForm
from django.contrib.contenttypes.models import ContentType

# from apps.book.models import BookCategory
# from apps.movie.models import Movie, MovieCategory
from apps.other.form import CommentForm
from apps.other.models import MeanList, Comment, Social, FriendLinks

register = template.Library()


# 获取菜单栏
@register.simple_tag
def get_meanList():
    means = MeanList.objects.all()
    return means


# 获取书籍数量
@register.simple_tag
def get_total_books():
    books_number = Article.objects.all().count()
    return books_number


# 获取文章分类
@register.simple_tag
def get_category():
    categories = ArticleCategory.objects.all()
    return categories



# 获取电影数量
# @register.simple_tag
# def get_total_movies():
#     books_number = Movie.objects.all().count()
#     return books_number


# 获取电影标签
# @register.simple_tag
# def get_movies_tags():
#     tags = MovieCategory.objects.annotate(movies_count=Count('movie')).order_by('-movies_count')
#     return tags


# 返回评论数量
@register.simple_tag
def get_comment_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return Comment.objects.filter(content_type=content_type, object_id=obj.id).count()


# 返回评论表单
@register.simple_tag
def get_comment_form(obj):
    content_type = ContentType.objects.get_for_model(obj)
    form = CommentForm(initial={'content_type': content_type.model, 'object_id': obj.pk, 'reply_comment_id': '0'})
    return form


# 返回评论表
@register.simple_tag
def get_comments_list(obj):
    content_type = ContentType.objects.get_for_model(obj)
    comments = Comment.objects.filter(content_type=content_type, object_id=obj.id, parent=None).order_by(
        '-comment_time')  # 获取所有与此类型相同的评论
    return comments


# 站长信息
@register.simple_tag
def get_social_media():
    try:
        social_media = Social.objects.get(id=1)
        return social_media
    except Social.DoesNotExist:
        return None


# 友情链接
@register.simple_tag
def get_friend_links():
    links = FriendLinks.objects.all()
    return links

