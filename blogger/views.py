from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Blogcomment
from django.contrib import messages
from .templatetags import extras


# Create your views here.
def bloggerhome(request):
    allposts = Post.objects.all()
    params = {'allposts': allposts}
    return render(request, 'blogger/bloggerhome.html', params)


def bloggerpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comments = Blogcomment.objects.filter(post=post)
    replies = Blogcomment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context = {'post': post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blogger/bloggerPost.html", context)


def postcomment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = Blogcomment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = Blogcomment.objects.get(sno=parentSno)
            comment = Blogcomment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")

    return redirect(f"/blogger/{post.slug}")
