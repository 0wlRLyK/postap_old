from betterforms.multiform import MultiModelForm, MultiForm
from django import forms
from django.forms.models import inlineformset_factory
from gallery.models import Gallery, GalleryItem

from .models import EntryNews, EntryArticle


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
        fields = ['name']


class GalleryItemForm(forms.ModelForm):
    class Meta:
        model = GalleryItem
        fields = ['image']


GalleryItemFormSet = inlineformset_factory(Gallery, GalleryItem, fields=['image'],
                                           form=GalleryItemForm, extra=5, max_num=5)


class NewsAddForm(MultiForm):
    form_classes = {
        'news': NewsForm,
        'gallery': GalleryForm,
        'item': GalleryItemFormSet,
    }


class NewsEditForm(MultiModelForm):
    form_classes = {
        'newsEntry': NewsForm,
        'gallery': GalleryForm,
        'item': GalleryItemFormSet,
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
