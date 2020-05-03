from django.urls import path

from .variables import NEWS, ARTICLES
from .views import HomePage, AddNews, ListNews, DetailNews, EditNews, EditGallery, DeleteNews, \
    ListArticles, DetailArticle, AddArticle, EditArticle, EditArticleGallery, DeleteArticle

urlpatterns = [
    path('', HomePage.as_view()),
    # ////--------
    # NEWS: НОВОСТИ
    # ////--------
    path(NEWS.mainURL(), ListNews.as_view()),
    path("{0}n/{1}/".format(NEWS.mainURL(), "<slug:slug>"), DetailNews.as_view()),
    path(NEWS.addURL(), AddNews.as_view()),
    path("{0}{1}/".format(NEWS.editURL(), "<int:pk>"), EditNews.as_view()),
    path("{0}{1}/".format(NEWS.editGalleryURL(), "<int:pk>"), EditGallery.as_view()),
    path("{0}{1}/".format(NEWS.delURL(), "<int:pk>"), DeleteNews.as_view()),
    # /////////-------
    # ARTICLES: СТАТЬИ
    # /////////-------
    path(ARTICLES.mainURL(), ListArticles.as_view()),
    path("{0}a/{1}/".format(ARTICLES.mainURL(), "<slug:slug>"), DetailArticle.as_view()),
    path(ARTICLES.addURL(), AddArticle.as_view()),
    path("{0}{1}/".format(ARTICLES.editURL(), "<int:pk>"), EditArticle.as_view()),
    path("{0}{1}/".format(ARTICLES.editGalleryURL(), "<int:pk>"), EditArticleGallery.as_view()),
    path("{0}{1}/".format(ARTICLES.delURL(), "<int:pk>"), DeleteArticle.as_view()),
]
