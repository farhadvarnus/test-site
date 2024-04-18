from django.urls import path
from .views import *
urlpatterns = [
    path("", index_blog, name='index_blog'),
    path("<int:pid>", single_blog, name='single_blog'),
]
