from notifications.models import Notification
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import reverse, redirect
from .models import Comment
from apps.other.form import CommentForm


# 消息通知页面
def my_notifications(request):
    context = {}
    return render(request, 'notice/my_notifications.html', context)


# 未读变已读，跳转至消息添加页面
def my_notification(request, my_notifications_pk):
    my_notification = get_object_or_404(Notification, pk=my_notifications_pk)
    my_notification.unread = False
    my_notification.save()
    return redirect(my_notification.data['url'])


# 删除全部已读
def delete_my_read_notifications(request):
    notifications = request.user.notifications.read()
    notifications.delete()
    return redirect(reverse('other:my_notifications'))


# 添加评论
def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('blog:index'))
    comment_form = CommentForm(request.POST, user=request.user)

    if comment_form.is_valid():
        # 检查通过，保存数据
        comment = Comment()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']
        parent = comment_form.cleaned_data['parent']

        if not parent is None:
            comment.root = parent.root if not parent.root is None else parent
            comment.parent = parent
            comment.reply_to = parent.user
        comment.save()

        # # 发送站内通知
        # # 判断评论的是博客还是
        # if comment.reply_to is None:
        #     # 接受者是文章
        #     recipient = comment.content_object.get_user()
        #     if comment.content_type.model == 'post':
        #         blog = comment.content_object
        #         verb = '{0} 评论了你的《{1}》'.format(comment.user,blog.title)
        #     else:
        #         raise Exception('不明评论')
        #
        # else:
        #     # 接受者是作者
        #     recipient = comment.reply_to
        #     verb = '{0} 评论了你的评论{1}'.format(comment.user, strip_tags(comment.parent.text))
        #
        # notify.send(comment.user, recipient=recipient, verb=verb, action_object=comment)

    return redirect(referer + '#comment')
