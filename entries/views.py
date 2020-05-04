from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView
from extra_views import UpdateWithInlinesView, InlineFormSetFactory
from gallery.models import Gallery
from gallery.models import GalleryItem

from .forms import NewsAddForm, ArticleAddForm, FileAddForm, ModAddForm, ImageGalleryAddForm
from .models import EntryNews, EntryArticle, EntryFile, EntryMod, EntryImageGallery
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


# //////-----
# MODS: МОДЫ
# //////-----


class ListMods(ListView):
    paginate_by = 2
    model = EntryMod
    context_object_name = "modsList"
    template_name = "entries/mods/list.html"


class DetailMod(DetailView):
    model = EntryMod
    context_object_name = "mod"
    template_name = "entries/mods/details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['some'] = GalleryItem.objects.filter(entry__entryfile__entrymod=self.object)
        return context


class AddMod(CreateView):
    form_class = ModAddForm
    success_url = "/mods/"
    template_name = "entries/mods/add.html"

    def form_valid(self, form):
        mods_form = form['mod'].save(commit=False)
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

        files_form.title = mods_form.title
        files_form.slug = "mod-{0}".format(mods_form.slug)
        files_form.save()
        mods_form.file = files_form
        mods_form.save()
        return redirect("/mods/")


class EditMod(UpdateView):
    success_url = "/mods/"
    template_name = "entries/mods/edit.html"
    model = EntryMod
    fields = '__all__'
    exclude = ['file']


class EditModFile(UpdateView):
    success_url = "/files/"
    template_name = "entries/mods/edit.html"
    model = EntryFile
    fields = '__all__'
    exclude = ['title', 'slug', 'objgallery', 'author']


class ImageModInline(InlineFormSetFactory):
    model = GalleryItem
    fields = ['image']


class EditModGallery(UpdateWithInlinesView):
    success_url = "/mods/"
    template_name = "entries/mods/edit.html"
    model = Gallery
    inlines = [ImageInline]
    fields = '__all__'


class DeleteMod(DeleteView):
    success_url = "/mods/"
    template_name = "entries/files/delete.html"
    model = Gallery


# /////////////---------------------
# IMAGEgALLERY: ГАЛЕРЕЯ ИЗОБРАЖЕНИЙ
# /////////////---------------------

class ListImages(ListView):
    paginate_by = 2
    model = EntryImageGallery
    context_object_name = "imagesList"
    template_name = "entries/gallery/list.html"


class DetailImage(DetailView):
    model = EntryImageGallery
    context_object_name = "image"
    template_name = "entries/gallery/details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['some'] = GalleryItem.objects.filter(entry__entryimagegallery=self.object)
        return context


class AddImage(CreateView):
    form_class = ImageGalleryAddForm
    success_url = "/gallery/"
    template_name = "entries/gallery/add.html"

    def form_valid(self, form):
        images_form = form['image_gallery'].save(commit=False)
        gallery = form['gallery'].save(commit=False)
        item = form['item'].save(commit=False)
        images_form.author = self.request.user
        gallery.name = images_form.title
        nid = EntryNews.objects.count()
        gallery.slug = "article{0}".format(nid + 1)
        images_form.objgallery = gallery
        gallery.save()
        for i in item:
            i.entry = gallery
            i.save()

        images_form.save()
        return redirect("/gallery/")


class EditImage(UpdateView):
    success_url = "/gallery/"
    template_name = "entries/gallery/edit.html"
    model = EntryImageGallery
    fields = "__all__"


class GalleryImageArticleInline(InlineFormSetFactory):
    model = GalleryItem
    fields = ['image']


class EditGalleryImage(UpdateWithInlinesView):
    success_url = "/gallery/"
    template_name = "entries/gallery/edit.html"
    model = Gallery
    inlines = [ImageInline]
    fields = '__all__'


class DeleteImage(DeleteView):
    success_url = "/gallery/"
    template_name = "entries/gallery/delete.html"
    model = Gallery
