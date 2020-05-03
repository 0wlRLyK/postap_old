from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView
from extra_views import UpdateWithInlinesView, InlineFormSetFactory
from gallery.models import GalleryItem

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


class DetailNews(DetailView):
    model = EntryNews
    context_object_name = "news"
    template_name = "temporary/test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = Gallery.objects.select_related()
        context['teachers'] = Gallery.objects.select_related()
        context['some'] = GalleryItem.objects.filter(entry__entrynews=self.object)
        return context


class AddNews(CreateView):
    form_class = NewsAddForm
    success_url = "news/"
    template_name = "entries/news/add.html"

    # def get_context_data(self, **kwargs):
    #     data = super(AddNews, self).get_context_data(**kwargs)
    #     if self.request.POST:
    #         data['sponsorships'] = GalleryItemFormSet(self.request.POST)
    #     else:
    #         data['sponsorships'] = GalleryItemFormSet()
    #     return data

    def form_valid(self, form):
        # context = self.get_context_data()
        # sponsorships = context['sponsorships']
        news_form = form['news'].save(commit=False)
        gallery = form['gallery'].save(commit=False)
        item = form['item'].save(commit=False)
        news_form.author = self.request.user
        gallery.name = news_form.title
        nid = EntryNews.objects.count()
        gallery.slug = "news{0}".format(nid + 1)

        # if sponsorships.is_valid():
        #     sponsorships.instance = self.object
        #     sponsorships.save()
        news_form.objgallery = gallery
        gallery.save()
        for i in item:
            i.entry = gallery
            i.save()

        news_form.save()
        return redirect("/news/")

    def get_success_url(self):
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
    fields = ['image', ]


class DeleteArticle(DeleteView):
    success_url = "/articles/"
    template_name = "entries/articles/delete.html"
    model = Gallery
