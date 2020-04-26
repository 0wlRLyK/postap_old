from django.urls import path

from .variables import NEWS, ARTICLES
from .views import HomePage, AddNews, ListNews, EditNews, EditGallery, DeleteNews, \
    ListArticles, AddArticle, EditArticle, EditGalleryArticle, DeleteArticle

urlpatterns = [
    path('', HomePage.as_view()),
    # ////--------
    # NEWS: НОВОСТИ
    # ////--------
    path(NEWS.mainURL(), ListNews.as_view()),
    path(NEWS.addURL(), AddNews.as_view()),
    path("{0}{1}/".format(NEWS.editURL(), "<int:pk>"), EditNews.as_view()),
    path("{0}{1}/".format(NEWS.editGalleryURL(), "<int:pk>"), EditGallery.as_view()),
    path("{0}{1}/".format(NEWS.delURL(), "<int:pk>"), DeleteNews.as_view()),
    # /////////-------
    # ARTICLES: СТАТЬИ
    # /////////-------
    path(ARTICLES.mainURL(), ListArticles.as_view()),
    path(ARTICLES.addURL(), AddArticle.as_view()),
    path("{0}{1}/".format(ARTICLES.editURL(), "<int:pk>"), EditArticle.as_view()),
    path("{0}{1}/".format(ARTICLES.editGalleryURL(), "<int:pk>"), EditGalleryArticle.as_view()),
    path("{0}{1}/".format(ARTICLES.delURL(), "<int:pk>"), DeleteArticle.as_view()),
]
