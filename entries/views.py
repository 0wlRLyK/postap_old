from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView
from extra_views import UpdateWithInlinesView, InlineFormSetFactory
from gallery.models import Gallery
from gallery.models import GalleryItem

from .forms import NewsAddForm, ArticleAddForm, FileAddForm
from .models import EntryNews, EntryArticle, EntryFile
from .variables import NEWS


class HomePage(TemplateView):
    template_name = 'temporary/home.html'
    extra_context = {
        "newsEntries": EntryNews.objects.filter(atMain=True, )[:5],
        "newsURL": NEWS.mainURL(),
    }


# ////--------
# NEWS: НОВОСТИ
# ////--------

class ListNews(ListView):
    paginate_by = 2
    model = EntryNews
    context_object_name = "newsList"
    template_name = "entries/news/list.html"


class DetailNews(DetailView):
    model = EntryNews
    context_object_name = "news"
    template_name = "entries/news/details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['some'] = GalleryItem.objects.filter(entry__entrynews=self.object)
        return context


class AddNews(CreateView):
    form_class = NewsAddForm
    success_url = "news/"
    template_name = "entries/news/add.html"

    def form_valid(self, form):
        news_form = form['news'].save(commit=False)
        gallery = form['gallery'].save(commit=False)
        item = form['item'].save(commit=False)
        news_form.author = self.request.user
        gallery.name = news_form.title
        nid = EntryNews.objects.count()
        gallery.slug = "news{0}".format(nid + 1)
        news_form.objgallery = gallery
        gallery.save()
        for i in item:
            i.entry = gallery
            i.save()

        news_form.save()
        return redirect("/news/")



class EditNews(UpdateView):
    success_url = "/news/"
    template_name = "entries/news/edit.html"
    model = EntryNews
    fields = ['title', 'slug', 'categories', 'shortDescript',
              'descript', 'image', 'inTop', 'atMain', 'source']


class ImageInline(InlineFormSetFactory):
    model = GalleryItem
    fields = ['image']


class EditGallery(UpdateWithInlinesView):
    success_url = "/news/"
    template_name = "entries/news/edit.html"
    model = Gallery
    inlines = [ImageInline]
    fields = '__all__'


class DeleteNews(DeleteView):
    success_url = "/news/"
    template_name = "entries/news/delete.html"
    model = Gallery


# /////////-------
# ARTICLES: СТАТЬИ
# /////////-------

class ListArticles(ListView):
    paginate_by = 2
    model = EntryArticle
    context_object_name = "articlesList"
    template_name = "entries/articles/list.html"


class DetailArticle(DetailView):
    model = EntryArticle
    context_object_name = "article"
    template_name = "entries/articles/details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['some'] = GalleryItem.objects.filter(entry__entryarticle=self.object)
        return context


class AddArticle(CreateView):
    form_class = ArticleAddForm
    success_url = "/articles/"
    template_name = "entries/articles/add.html"

    def form_valid(self, form):
        articles_form = form['article'].save(commit=False)
        gallery = form['gallery'].save(commit=False)
        item = form['item'].save(commit=False)
        articles_form.author = self.request.user
        gallery.name = articles_form.title
        nid = EntryNews.objects.count()
        gallery.slug = "article{0}".format(nid + 1)
        articles_form.objgallery = gallery
        gallery.save()
        for i in item:
            i.entry = gallery
            i.save()

        articles_form.save()
        return redirect("/articles/")


class EditArticle(UpdateView):
    success_url = "/articles/"
    template_name = "entries/articles/edit.html"
    model = EntryArticle
    fields = ['title', 'slug', 'categories', 'shortDescript',
              'descript', 'image', 'inTop', 'atMain', 'source']


class ImageArticleInline(InlineFormSetFactory):
    model = GalleryItem
    fields = ['image']


class EditArticleGallery(UpdateWithInlinesView):
    success_url = "/article/"
    template_name = "entries/articles/edit.html"
    model = Gallery
    inlines = [ImageInline]
    fields = '__all__'


class DeleteArticle(DeleteView):
    success_url = "/articles/"
    template_name = "entries/articles/delete.html"
    model = Gallery


# //////-------
# FILES: ФАЙЛЫ
# //////-------
class ListFiles(ListView):
    paginate_by = 2
    model = EntryFile
    context_object_name = "filesList"
    template_name = "entries/files/list.html"


class DetailFile(DetailView):
    model = EntryFile
    context_object_name = "file"
    template_name = "entries/files/details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['some'] = GalleryItem.objects.filter(entry__entryfile=self.object)
        return context


class AddFile(CreateView):
    form_class = FileAddForm
    success_url = "/files/"
    template_name = "entries/files/add.html"

    def form_valid(self, form):
        files_form = form['file'].save(commit=False)
        gallery = form['gallery'].save(commit=False)
        item = form['item'].save(commit=False)
        files_form.author = self.request.user
        gallery.name = files_form.title
        nid = EntryNews.objects.count()
        gallery.slug = "file{0}".format(nid + 1)
        files_form.objgallery = gallery
        gallery.save()
        for i in item:
            i.entry = gallery
            i.save()

        files_form.save()
        return redirect("/files/")


class EditFile(UpdateView):
    success_url = "/files/"
    template_name = "entries/files/edit.html"
    model = EntryFile
    fields = '__all__'
    exclude = ['objgallery', 'author']


class ImageFileInline(InlineFormSetFactory):
    model = GalleryItem
    fields = ['image']


class EditFileGallery(UpdateWithInlinesView):
    success_url = "/files/"
    template_name = "entries/files/edit.html"
    model = Gallery
    inlines = [ImageInline]
    fields = '__all__'


class DeleteFile(DeleteView):
    success_url = "/files/"
    template_name = "entries/files/delete.html"
    model = Gallery
