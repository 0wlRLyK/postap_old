from django.urls import path

from .variables import NEWS, ARTICLES, FILES
from .views import HomePage, AddNews, ListNews, DetailNews, EditNews, EditGallery, DeleteNews, \
    ListArticles, DetailArticle, AddArticle, EditArticle, EditArticleGallery, DeleteArticle, \
    ListFiles, DetailFile, AddFile, EditFile, EditFileGallery, DeleteFile

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
    # //////-------
    # FILES: ФАЙЛЫ
    # //////-------
    path(FILES.mainURL(), ListFiles.as_view()),
    path("{0}f/{1}/".format(FILES.mainURL(), "<slug:slug>"), DetailFile.as_view()),
    path(FILES.addURL(), AddFile.as_view()),
    path("{0}{1}/".format(FILES.editURL(), "<int:pk>"), EditFile.as_view()),
    path("{0}{1}/".format(FILES.editGalleryURL(), "<int:pk>"), EditFileGallery.as_view()),
    path("{0}{1}/".format(FILES.delURL(), "<int:pk>"), DeleteFile.as_view()),
]
