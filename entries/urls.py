from django.urls import path

from .variables import NEWS
from .views import HomePage, AddNews, ListNews, EditNews, EditGallery, DeleteNews

urlpatterns = [
    path('', HomePage.as_view()),
    path(NEWS.module_list(), ListNews.as_view()),
    path(NEWS.module_adding(), AddNews.as_view()),
    path("news/edit/<int:pk>/", EditNews.as_view()),
    path("news/edit_gallery/<int:pk>/", EditGallery.as_view()),
    path("news/del/<int:pk>/", DeleteNews.as_view()),
]
