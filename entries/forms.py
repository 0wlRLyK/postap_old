from betterforms.multiform import MultiForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.forms.models import inlineformset_factory
from gallery.models import Gallery, GalleryItem

from .models import News, Article, File, Mod, ImageGallery, Guide, Faq


# ////--------
# NEWS: НОВОСТИ
# ////--------


class NewsForm(forms.ModelForm):
    short_descript = forms.CharField(widget=CKEditorUploadingWidget())
    descript = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = ['title', 'slug', 'categories', 'short_descript',
                  'descript', 'image', 'in_top', 'at_main', 'source', 'tags']


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['name']
        # exclude = ['name']


class GalleryItemForm(forms.ModelForm):
    class Meta:
        model = GalleryItem
        fields = "__all__"


GalleryItemFormSet = inlineformset_factory(Gallery, GalleryItem,
                                           form=GalleryItemForm, extra=5, max_num=5)


class NewsAddForm(MultiForm):
    form_classes = {
        'news': NewsForm,
        'gallery': GalleryForm,
        'item': GalleryItemFormSet,
    }




# /////////-------
# ARTICLES: СТАТЬИ
# /////////-------


class ArticleForm(forms.ModelForm):
    short_descript = forms.CharField(widget=CKEditorUploadingWidget())
    descript = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = ['title', 'slug', 'categories', 'short_descript',
                  'descript', 'image', 'in_top', 'at_main', 'source', 'tags']


class ArticleAddForm(MultiForm):
    form_classes = {
        'article': ArticleForm,
        'gallery': GalleryForm,
        'item': GalleryItemFormSet,
    }


# //////-------
# FILES: ФАЙЛЫ
# //////-------


class FileForm(forms.ModelForm):
    short_descript = forms.CharField(widget=CKEditorUploadingWidget())
    descript = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = File
        fields = '__all__'
        exclude = ['objgallery', 'author']


class FileAddForm(MultiForm):
    form_classes = {
        'file': FileForm,
        'gallery': GalleryForm,
        'item': GalleryItemFormSet,
    }


# //////-----
# MODS: МОДЫ
# //////-----

class FileModForm(forms.ModelForm):
    short_descript = forms.CharField(widget=CKEditorUploadingWidget())
    descript = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = File
        fields = '__all__'
        exclude = ['title', 'slug', 'objgallery', 'author']


class ModForm(forms.ModelForm):
    plot = forms.CharField(widget=CKEditorUploadingWidget())
    features = forms.CharField(widget=CKEditorUploadingWidget())
    innovations = forms.CharField(widget=CKEditorUploadingWidget())
    gameplay = forms.CharField(widget=CKEditorUploadingWidget())
    locations = forms.CharField(widget=CKEditorUploadingWidget())
    weapons = forms.CharField(widget=CKEditorUploadingWidget())
    other = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Mod
        fields = '__all__'
        exclude = ['file', 'vote_score', 'num_vote_up', 'num_vote_down']


class ModAddForm(MultiForm):
    form_classes = {
        'mod': ModForm,
        'file': FileModForm,
        'gallery': GalleryForm,
        'item': GalleryItemFormSet,
    }


# /////////////---------------------
# IMAGEgALLERY: ГАЛЕРЕЯ ИЗОБРАЖЕНИЙ
# /////////////---------------------


class ImageGalleryForm(forms.ModelForm):
    short_descript = forms.CharField(widget=CKEditorUploadingWidget())
    descript = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = ImageGallery
        fields = '__all__'
        exclude = ['objgallery', 'author']


class ImageGalleryAddForm(MultiForm):
    form_classes = {
        'image_gallery': ImageGalleryForm,
        'gallery': GalleryForm,
        'item': GalleryItemFormSet,
    }


# ///////----------------------
# GUIDES: ГАЙДЫ ПО ПРОХОЖДЕНИЮ
# ///////----------------------


class GuideItemForm(forms.ModelForm):
    descript = forms.CharField(widget=CKEditorUploadingWidget())
    solution = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Guide
        fields = '__all__'


class GuideKostilForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ['mod']


GuideFormSet = inlineformset_factory(Mod, Guide, form=GuideItemForm, extra=5, max_num=5, min_num=1)


class GuidesAddForm(MultiForm):
    form_classes = {
        'guide': GuideKostilForm,
        'guides': GuideFormSet,
    }


# ////--------------------------
# FAQ: ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ
# ////--------------------------
class FaqForm(forms.ModelForm):
    questionDescript = forms.CharField(widget=CKEditorUploadingWidget())
    answer = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Faq
        fields = '__all__'
        exclude = ['objgallery', 'author']


class FaqAskForm(forms.ModelForm):
    questionDescript = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Faq
        fields = '__all__'
        exclude = ['objgallery', 'author', 'answer']


class FaqAnswerForm(forms.ModelForm):
    question = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    questionDescript = forms.CharField(widget=CKEditorUploadingWidget(attrs={'readonly': 'readonly'}))
    answer = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Faq
        fields = '__all__'
        exclude = ['objgallery', 'author', 'answer']


class FaqAddForm(MultiForm):
    form_classes = {
        'faq': FaqForm,
        'gallery': GalleryForm,
        'item': GalleryItemFormSet,
    }


class FaqAskAddForm(MultiForm):
    form_classes = {
        'faq': FaqAskForm,
        'gallery': GalleryForm,
        'item': GalleryItemFormSet,
    }
