from django.urls import path
from .views import *
urlpatterns = [
    path("", index_blog, name='index_blog'),
    path("single/", single_blog, name='single_blog'),
]
