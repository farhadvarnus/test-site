from django.shortcuts import render
from blog.models import Post
# Create your views here.
from django.utils import timezone
from .forms import ContactForm, NewsletterForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def index_view(request):

    return render(request, "website/index.html")


def about_view(request):
    return render(request, "website/about.html")


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.instance.name = "unknown"
            form.save()
            messages.add_message(request, messages.SUCCESS, 'SUCCESS!!!')
            return HttpResponseRedirect("/")

        else:
            messages.add_message(request, messages.ERROR, 'FAILD!!!')
            return HttpResponseRedirect("/")

    form = ContactForm()
    return render(request, "website/contact.html", {"form": form})


def elements_view(request):
    return render(request, "website/elements.html")


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'SUCCESS!!!')
            return HttpResponseRedirect("/")

        else:
            messages.add_message(request, messages.ERROR, 'FAILD!!!')
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")


def test(request):
    post = Post.objects.filter(
        published_date__lte=timezone.now())
    post1 = Post.objects.all()
    p = Post.objects.all()[0]
    p.counted_view += 1
    p.save()
    context = {"post": post, "post1": post1}
    return render(request, "test.html", context)
