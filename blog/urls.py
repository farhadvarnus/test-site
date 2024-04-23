from django.urls import path
from .views import *
urlpatterns = [
    path("", index_blog, name='index_blog'),
    path("<int:pid>", single_blog, name='single_blog'),
    path("category/<str:cat_name>", index_blog, name='category_blog'),
    path("author/<str:author_username>", index_blog, name='author_blog'),
    path("search/", search_blog, name='search_blog'),
]
