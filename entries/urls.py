from django.urls import path

from .variables import NEWS, ARTICLES, FILES, MODS, IMAGE_GALLERY, GUIDES
from .views import HomePage, AddNews, ListNews, DetailNews, EditNews, EditGallery, DeleteNews, \
    ListArticles, DetailArticle, AddArticle, EditArticle, EditArticleGallery, DeleteArticle, \
    ListFiles, DetailFile, AddFile, EditFile, EditFileGallery, DeleteFile, \
    ListMods, DetailMod, AddMod, EditMod, EditModFile, EditModGallery, DeleteMod, \
    ListImages, DetailImage, AddImage, EditImage, EditGalleryImage, DeleteImage, \
    ListGuides, ListModsGuides, AddGuide, EditGuide, DeleteGuide, \
    ListQuestions, AddQuestion, AskQuestion, EditQuestion, EditUserQuestion, AnswerQuestion, EditFaqGallery, DeleteFaq

app_name = 'entries_app'
urlpatterns = [
    path('', HomePage.as_view()),
    # ////--------
    # NEWS: НОВОСТИ
    # ////--------
    path(NEWS.mainURL(), ListNews.as_view(), name="news_list"),
    path("{0}n/{1}/".format(NEWS.detailURL(), "<slug:slug>"), DetailNews.as_view(), name="news_details"),
    path(NEWS.addURL(), AddNews.as_view(), name="news_add"),
    path("{0}{1}/".format(NEWS.editURL(), "<int:pk>"), EditNews.as_view(), name="news_edit"),
    path("{0}{1}/".format(NEWS.editGalleryURL(), "<int:pk>"), EditGallery.as_view(), name="news_edit_gal"),
    path("{0}{1}/".format(NEWS.delURL(), "<int:pk>"), DeleteNews.as_view(), name="news_del"),
    # /////////-------
    # ARTICLES: СТАТЬИ
    # /////////-------
    path(ARTICLES.mainURL(), ListArticles.as_view(), name="article_list"),
    path("{0}{1}/".format(ARTICLES.detailURL(), "<slug:slug>"), DetailArticle.as_view(), name="article_details"),
    path(ARTICLES.addURL(), AddArticle.as_view(), name="article_add"),
    path("{0}{1}/".format(ARTICLES.editURL(), "<int:pk>"), EditArticle.as_view(), name="article_edit"),
    path("{0}{1}/".format(ARTICLES.editGalleryURL(), "<int:pk>"), EditArticleGallery.as_view(),
         name="article_edit_gal"),
    path("{0}{1}/".format(ARTICLES.delURL(), "<int:pk>"), DeleteArticle.as_view(), name="article_del"),
    # //////-------
    # FILES: ФАЙЛЫ
    # //////-------
    path(FILES.mainURL(), ListFiles.as_view(), name="file_list"),
    path("{0}{1}/".format(FILES.detailURL(), "<slug:slug>"), DetailFile.as_view(), name="file_details"),
    path(FILES.addURL(), AddFile.as_view(), name="file_add"),
    path("{0}{1}/".format(FILES.editURL(), "<int:pk>"), EditFile.as_view(), name="file_edit"),
    path("{0}{1}/".format(FILES.editGalleryURL(), "<int:pk>"), EditFileGallery.as_view(), name="file_edit_gal"),
    path("{0}{1}/".format(FILES.delURL(), "<int:pk>"), DeleteFile.as_view(), name="file_del"),
    # //////-----
    # MODS: МОДЫ
    # //////-----
    path(MODS.mainURL(), ListMods.as_view(), name="mod_list"),
    path("{0}{1}/".format(MODS.detailURL(), "<slug:slug>"), DetailMod.as_view(), name="mod_details"),
    path(MODS.addURL(), AddMod.as_view(), name="mod_add"),
    path("{0}file/{1}/".format(MODS.detailURL(), "<int:pk>"), EditModFile.as_view(), name="mod_edit_file"),
    path("{0}{1}/".format(MODS.editURL(), "<int:pk>"), EditMod.as_view(), name="mod_edit"),
    path("{0}{1}/".format(MODS.editGalleryURL(), "<int:pk>"), EditModGallery.as_view(), name="mod_edit_gal"),
    path("{0}{1}/".format(MODS.delURL(), "<int:pk>"), DeleteMod.as_view(), name="mod_del"),
    # /////////////---------------------
    # IMAGEgALLERY: ГАЛЕРЕЯ ИЗОБРАЖЕНИЙ
    # /////////////---------------------
    path(IMAGE_GALLERY.mainURL(), ListImages.as_view(), name="gallery_list"),
    path("{0}{1}/".format(IMAGE_GALLERY.detailURL(), "<slug:slug>"), DetailImage.as_view(), name="gallery_details"),
    path(IMAGE_GALLERY.addURL(), AddImage.as_view(), name="gallery_add"),
    path("{0}{1}/".format(IMAGE_GALLERY.editURL(), "<int:pk>"), EditImage.as_view(), name="gallery_edit"),
    path("{0}{1}/".format(IMAGE_GALLERY.editGalleryURL(), "<int:pk>"), EditGalleryImage.as_view(),
         name="gallery_edit_gal"),
    path("{0}{1}/".format(IMAGE_GALLERY.delURL(), "<int:pk>"), DeleteImage.as_view(), name="gallery_del"),
    # ///////----------------------
    # GUIDES: ГАЙДЫ ПО ПРОХОЖДЕНИЮ
    # ///////----------------------
    path(GUIDES.mainURL(), ListModsGuides.as_view(), name="guide_list"),
    path("{0}{1}/".format(GUIDES.detailURL(), "<int:pk>"), ListGuides.as_view(), name="guide_details"),
    path(GUIDES.addURL(), AddGuide.as_view(), name="guide_add"),
    path("{0}{1}/".format(GUIDES.editURL(), "<int:pk>"), EditGuide.as_view(), name="guide_edit"),
    path("{0}{1}/".format(GUIDES.delURL(), "<int:pk>"), DeleteGuide.as_view(), name="guide_del"),
    # ////--------------------------
    # FAQ: ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ
    # ////--------------------------
    path("faq/", ListQuestions.as_view(), name="faq_list"),
    path("faq/add/", AddQuestion.as_view(), name="faq_add"),
    path("faq/ask/", AskQuestion.as_view(), name="faq_ask"),
    path("faq/edit/<int:pk>", EditQuestion.as_view(), name="faq_edit"),
    path("faq/edit/u/<int:pk>", EditUserQuestion.as_view(), name="faq_edit_by_user"),
    path("faq/answer/<int:pk>", AnswerQuestion.as_view(), name="faq_answer"),
    path("faq/edit_gallery/<int:pk>", EditFaqGallery.as_view(), name="faq_edit_gal"),
    path("faq/del/<int:pk>", DeleteFaq.as_view(), name="faq_del"),
]
