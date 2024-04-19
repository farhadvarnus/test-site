from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
# Create your views here.


def index_blog(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now(), status=1)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def single_blog(request, pid):
    posts = Post.objects.filter(
        published_date__lte=timezone.now(), status=1)
    post = get_object_or_404(posts, pk=pid)
    post.counted_view += 1
    post.save()

    nex = False
    next = 404
    prev_post = 404
    next_post = 404

    for i, po in enumerate(posts):
        if nex:
            next = po.id
            break
        if po.id == post.id:
            if i == 0:
                prev = 404
            if i != 0:
                prev = temp
            nex = True

        temp = po.id
    if next != 404:
        next_post = get_object_or_404(posts, pk=next)
    if prev != 404:
        prev_post = get_object_or_404(posts, pk=prev)
    context = {"post": post, 'posts': posts,
               "next": next_post, "prev": prev_post}
    return render(request, "blog/blog-single.html", context)
