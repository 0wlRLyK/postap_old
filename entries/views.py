from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView

from .forms import NewsAddForm, ArticleAddForm
from .models import EntryNews, Gallery, EntryArticle
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


class AddNews(CreateView):
    form_class = NewsAddForm
    success_url = "news/"
    template_name = "entries/news/add.html"

    def form_valid(self, form):
        # Save the user first, because the profile needs a user before it
        # can be saved.

        newsEntry = form['newsEntry'].save(commit=False)
        gallery = form['gallery'].save(commit=False)
        gallery.title = newsEntry.title
        gallery.entry = ContentType.objects.get(model="entrynews")
        gallery.slug = "news"
        gallery.save()
        newsEntry.author = self.request.user
        newsEntry.gallery = gallery
        newsEntry.save()
        return redirect("/news/")


class EditNews(UpdateView):
    success_url = "/news/"
    template_name = "entries/news/edit.html"
    model = EntryNews
    fields = ['title', 'slug', 'categories', 'shortDescript',
              'descript', 'image', 'inTop', 'atMain', 'source']


class EditGallery(UpdateView):
    success_url = "/news/"
    template_name = "entries/news/edit.html"
    model = Gallery
    fields = ['image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9',
              'image10', 'image11', 'image12', 'image13', 'image14', 'image15']


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


class AddArticle(CreateView):
    form_class = ArticleAddForm
    success_url = "/articles/"
    template_name = "entries/articles/add.html"

    def form_valid(self, form):
        articlesEntry = form['articlesEntry'].save(commit=False)
        gallery = form['gallery'].save(commit=False)
        gallery.title = articlesEntry.title
        gallery.entry = ContentType.objects.get(model="entryarticle")
        gallery.slug = "articles"
        gallery.save()
        articlesEntry.author = self.request.user
        articlesEntry.gallery = gallery
        articlesEntry.save()
        return redirect("/articles/")


class EditArticle(UpdateView):
    success_url = "/articles/"
    template_name = "entries/articles/edit.html"
    model = EntryArticle
    fields = ['title', 'slug', 'categories', 'shortDescript',
              'descript', 'image', 'inTop', 'atMain', 'source']


class EditGalleryArticle(UpdateView):
    success_url = "/articles/"
    template_name = "entries/articles/edit.html"
    model = Gallery
    fields = ['image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9',
              'image10', 'image11', 'image12', 'image13', 'image14', 'image15']


class DeleteArticle(DeleteView):
    success_url = "/articles/"
    template_name = "entries/articles/delete.html"
    model = Gallery
