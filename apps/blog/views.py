from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.shortcuts import render, get_object_or_404, HttpResponse
import markdown

# 博客页

from django.views.generic import ListView

from apps.blog.models import Article, ArticleCategory


class ArticleIndex(ListView):
    template_name = "blog/index.html"  # 指定显示的页面
    context_object_name = "posts"  # 在前端页面的参数名称

    def get_queryset(self):  # 传递给index.html的内容, 在html页面中使用posts表示
        """Return the last five published questions."""
        return Article.objects.filter(status='n')


# 分类
class Categories(ArticleIndex):
    template_name = 'blog/category_list.html'  # 跳转到category_list.html
    paginate_by = None  # 每页显示的数量, 这里是全部显示

    # 额外传递一些信息
    def get_context_data(self, **kwargs):
        self.cate_count = ArticleCategory.objects.all().count()
        kwargs['cate_count'] = self.cate_count
        return super(Categories, self).get_context_data(**kwargs)


# 各分类下的文章列表
class CategoryView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        cate = get_object_or_404(ArticleCategory, pk=self.kwargs.get('pk'))  # url中匹配的参数传递给pk
        self.cate_name = cate.name
        return Article.objects.filter(category=cate)

    def get_context_data(self, **kwargs):
        kwargs['cate_name'] = self.cate_name
        return super(CategoryView, self).get_context_data(**kwargs)


def article(request, pk):
    post = get_object_or_404(Article, pk=pk)
    author = User.objects.get(id=post.author_id)
    category = ArticleCategory.objects.get(id=post.category_id)
    post.increase_views()  # 阅读量加1
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'markdown.extensions.fenced_code',

    ])

    post.body = md.convert(post.body)
    if strip_tags(md.toc).strip() == '':
        post.toc = ''
    else:
        post.toc = md.toc

    # 获取相关文章
    relative_posts = Article.objects.filter(category_id=post.category_id, status='p').exclude(pk=pk).order_by('?')[:4]

    context = {}
    context['post'] = post
    context['author'] = author
    context['category'] = category
    context['relative_posts'] = relative_posts
    return render(request, 'blog/article.html', context)
