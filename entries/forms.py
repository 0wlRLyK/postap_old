from betterforms.multiform import MultiModelForm, MultiForm
from django import forms

from .models import EntryNews, Gallery, EntryArticle


# ////--------
# NEWS: НОВОСТИ
# ////--------


class NewsForm(forms.ModelForm):
    class Meta:
        model = EntryNews
        fields = ['title', 'slug', 'categories', 'shortDescript',
                  'descript', 'image', 'inTop', 'atMain', 'source']


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9',
                  'image10', 'image11', 'image12', 'image13', 'image14', 'image15']


class NewsAddForm(MultiForm):
    form_classes = {
        'newsEntry': NewsForm,
        'gallery': GalleryForm,
    }


class NewsEditForm(MultiModelForm):
    form_classes = {
        'newsEntry': NewsForm,
        'gallery': GalleryForm,
    }


# /////////-------
# ARTICLES: СТАТЬИ
# /////////-------


class ArticleForm(forms.ModelForm):
    class Meta:
        model = EntryArticle
        fields = ['title', 'slug', 'categories', 'shortDescript',
                  'descript', 'image', 'inTop', 'atMain', 'source']


class ArticleAddForm(MultiForm):
    form_classes = {
        'articlesEntry': ArticleForm,
        'gallery': GalleryForm,
    }
