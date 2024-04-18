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
    post = get_object_or_404(Post, pk=pid)
    post.counted_view += 1
    post.save()
    context = {"post": post}
    return render(request, "blog/blog-single.html", context)
