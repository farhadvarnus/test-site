from django import template
from blog.models import Post, Category
from django.utils import timezone

register = template.Library()


@register.simple_tag(name="totalposts")
def func():
    posts = Post.objects.filter(
        status=1, published_date__lte=timezone.now()).count()
    return posts


@register.inclusion_tag("blog/blog-lastest-post.html")
def lastest_posts(arg=3):
    posts = Post.objects.filter(
        published_date__lte=timezone.now(), status=1).order_by("created_date")[:arg]
    return {"posts": posts}


@register.inclusion_tag('blog/blog-categories.html')
def postcategories():
    posts = Post.objects.filter(
        status=1, published_date__lte=timezone.now())
    categories = Category.objects.all()
    dic_cat = {}
    for name in categories:
        dic_cat[name] = posts.filter(category=name).count()
    return {'categories': dic_cat}
