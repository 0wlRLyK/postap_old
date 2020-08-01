from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from entries.models import News, Article, File, ImageGallery, Guide, Faq

from . import views
from .models import LikeDislike

app_name = 'ajax'
urlpatterns = [
    url(r'^news/(?P<pk>\d+)/like/$',
        login_required(views.VotesView.as_view(model=News, vote_type=LikeDislike.LIKE)),
        name='news_like'),
    url(r'^news/(?P<pk>\d+)/dislike/$',
        login_required(views.VotesView.as_view(model=News, vote_type=LikeDislike.DISLIKE)),
        name='news_dislike'),

    url(r'^article/(?P<pk>\d+)/like/$',
        login_required(views.VotesView.as_view(model=Article, vote_type=LikeDislike.LIKE)),
        name='article_like'),
    url(r'^article/(?P<pk>\d+)/dislike/$',
        login_required(views.VotesView.as_view(model=Article, vote_type=LikeDislike.DISLIKE)),
        name='article_dislike'),

    url(r'^files/(?P<pk>\d+)/like/$',
        login_required(views.VotesView.as_view(model=File, vote_type=LikeDislike.LIKE)),
        name='file_like'),
    url(r'^files/(?P<pk>\d+)/dislike/$',
        login_required(views.VotesView.as_view(model=File, vote_type=LikeDislike.DISLIKE)),
        name='file_dislike'),

    url(r'^gallery/(?P<pk>\d+)/like/$',
        login_required(views.VotesView.as_view(model=ImageGallery, vote_type=LikeDislike.LIKE)),
        name='gallery_like'),
    url(r'^gallery/(?P<pk>\d+)/dislike/$',
        login_required(views.VotesView.as_view(model=ImageGallery, vote_type=LikeDislike.DISLIKE)),
        name='gallery_dislike'),

    url(r'^guide/(?P<pk>\d+)/like/$',
        login_required(views.VotesView.as_view(model=Guide, vote_type=LikeDislike.LIKE)),
        name='guide_like'),
    url(r'^gudie/(?P<pk>\d+)/dislike/$',
        login_required(views.VotesView.as_view(model=Guide, vote_type=LikeDislike.DISLIKE)),
        name='guide_dislike'),

    url(r'^faq/(?P<pk>\d+)/like/$',
        login_required(views.VotesView.as_view(model=Faq, vote_type=LikeDislike.LIKE)),
        name='guide_like'),
    url(r'^faq/(?P<pk>\d+)/dislike/$',
        login_required(views.VotesView.as_view(model=Faq, vote_type=LikeDislike.DISLIKE)),
        name='guide_dislike'),
]
