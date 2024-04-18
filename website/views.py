from django.shortcuts import render
from blog.models import Post
# Create your views here.
from django.utils import timezone


def index_view(request):
    return render(request, "website/index.html")


def about_view(request):
    return render(request, "website/about.html")


def contact_view(request):
    return render(request, "website/contact.html")


def elements_view(request):
    return render(request, "website/elements.html")


def test(request):
    post = Post.objects.filter(
        published_date__lte=timezone.now())
    post1 = Post.objects.all()
    p = Post.objects.all()[0]
    p.counted_view += 1
    p.save()
    context = {"post": post, "post1": post1}
    return render(request, "test.html", context)
