from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView
from extra_views import UpdateWithInlinesView, InlineFormSetFactory
from gallery.models import Gallery
from gallery.models import GalleryItem
from hitcount.views import HitCountDetailView

from .forms import NewsForm, NewsAddForm, ArticleForm, ArticleAddForm, FileForm, FileAddForm, FileModForm, \
    ModForm, ModAddForm, ImageGalleryForm, ImageGalleryAddForm, GuidesAddForm, FaqAddForm, FaqAskAddForm, \
    FaqAnswerForm, FaqForm, FaqAskForm
from .models import News, Article, File, Mod, ImageGallery, Guide, Faq
from .variables import NEWS


class HomePage(TemplateView):
    template_name = 'temporary/home.html'
    extra_context = {
        "newsEntries": News.objects.filter(at_main=True, )[:5],
        "newsURL": NEWS.mainURL(),
    }


# ////--------
# NEWS: НОВОСТИ
# ////--------

class ListNews(ListView):
    paginate_by = 2
    model = News
    context_object_name = "newsList"
    template_name = "entries/news/list.html"


class DetailNews(HitCountDetailView):
    model = News
    context_object_name = "news"
    template_name = "entries/news/details.html"
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['some'] = GalleryItem.objects.filter(entry__news=self.object)
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
        nid = News.objects.count()
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
    form_class = NewsForm
    model = News


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
    model = Article
    context_object_name = "articlesList"
    template_name = "entries/articles/list.html"


class DetailArticle(DetailView):
    model = Article
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
        nid = Article.objects.count()
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
    model = Article
    form_class = ArticleForm


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
    model = File
    context_object_name = "filesList"
    template_name = "entries/files/list.html"


class DetailFile(DetailView):
    model = File
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
        nid = File.objects.count()
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
    model = File
    form_class = FileForm


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
    model = Mod
    context_object_name = "modsList"
    template_name = "entries/mods/list.html"


class DetailMod(DetailView):
    model = Mod
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
        nid = Mod.objects.count()
        gallery.slug = "mod{0}".format(nid + 1)
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
    model = Mod
    form_class = ModForm


class EditModFile(UpdateView):
    success_url = "/files/"
    template_name = "entries/mods/edit.html"
    model = File
    form_class = FileModForm


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
    model = ImageGallery
    context_object_name = "imagesList"
    template_name = "entries/gallery/list.html"


class DetailImage(DetailView):
    model = ImageGallery
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
        gallery.name = images_form.name
        nid = ImageGallery.objects.count()
        gallery.slug = "gallery{0}".format(nid + 1)
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
    model = ImageGallery
    form_class = ImageGalleryForm


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


# ///////----------------------
# GUIDES: ГАЙДЫ ПО ПРОХОЖДЕНИЮ
# ///////----------------------

class ListModsGuides(ListView):
    paginate_by = 2
    context_object_name = "mods"
    template_name = "entries/guides/list_mods.html"
    queryset = Mod.objects.filter(modguides__isnull=False).distinct()


class ListGuides(DetailView):
    context_object_name = "mod"
    template_name = "entries/guides/list.html"
    model = Mod

    def get_context_data(self, **kwargs):
        context = super(ListGuides, self).get_context_data(**kwargs)
        activities = self.get_related_activities()
        context['related_activities'] = activities
        context['page_obj'] = activities
        return context

    def get_related_activities(self):
        queryset = Guide.objects.filter(mod=self.get_object())
        paginator = Paginator(queryset, 2)  # paginate_by
        page = self.request.GET.get('page')
        activities = paginator.get_page(page)
        return activities

    # def get_context_data(self, **kwargs):
    #     object_list = Guide.objects.filter(mod=self.get_object())
    #     context = super(ListGuides, self).get_context_data(object_list=object_list, **kwargs)
    #     return context


class DetailGuide(DetailView):
    model = Guide
    context_object_name = "guide"
    template_name = "entries/guides/details.html"


class AddGuide(CreateView):
    form_class = GuidesAddForm
    success_url = "/guides/"
    template_name = "entries/guides/add.html"

    def form_valid(self, form):
        guide = form['guide'].save(commit=False)
        guides_form = form['guides'].save(commit=False)
        for g in guides_form:
            g.mod = guide.mod
            g.save()
        return redirect("/guides/")


class EditGuide(UpdateView):
    success_url = "/guides/"
    template_name = "entries/guides/edit.html"
    model = Guide
    fields = '__all__'


class DeleteGuide(DeleteView):
    success_url = "/guides/"
    template_name = "entries/guides/delete.html"
    model = Guide


# ////--------------------------
# FAQ: ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ
# ////--------------------------

class ListQuestions(ListView):
    paginate_by = 2
    model = Faq
    context_object_name = "faqList"
    template_name = "entries/faq/list.html"


# class DetailFile(DetailView):
#     model = File
#     context_object_name = "file"
#     template_name = "entries/files/details.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['some'] = GalleryItem.objects.filter(entry__entryfile=self.object)
#         return context


class AddQuestion(CreateView):
    form_class = FaqAddForm
    success_url = "/faq/"
    template_name = "entries/faq/add.html"

    def form_valid(self, form):
        faq_form = form['faq'].save(commit=False)
        gallery = form['gallery'].save(commit=False)
        item = form['item'].save(commit=False)
        faq_form.author = self.request.user
        gallery.name = faq_form.question
        nid = Faq.objects.count()
        gallery.slug = "faq{0}".format(nid + 1)
        faq_form.objgallery = gallery
        gallery.save()
        for i in item:
            i.entry = gallery
            i.save()

        faq_form.save()
        return redirect("/faq/")


class AskQuestion(CreateView):
    form_class = FaqAskAddForm
    success_url = "/faq/"
    template_name = "entries/faq/add.html"

    def form_valid(self, form):
        faq_form = form['faq'].save(commit=False)
        gallery = form['gallery'].save(commit=False)
        item = form['item'].save(commit=False)
        faq_form.author = self.request.user
        gallery.name = faq_form.question
        nid = Faq.objects.count()
        gallery.slug = "faq{0}".format(nid + 1)
        faq_form.objgallery = gallery
        gallery.save()
        for i in item:
            i.entry = gallery
            i.save()

        faq_form.save()
        return redirect("/faq/")


class EditQuestion(UpdateView):
    success_url = "/faq/"
    template_name = "entries/faq/edit.html"
    model = Faq
    form_class = FaqForm


class EditUserQuestion(UpdateView):
    success_url = "/faq/"
    template_name = "entries/faq/edit.html"
    model = Faq
    form_class = FaqAskForm


class AnswerQuestion(UpdateView):
    success_url = "/faq/"
    template_name = "entries/files/edit.html"
    model = Faq
    form_class = FaqAnswerForm


class ImageFaqInline(InlineFormSetFactory):
    model = GalleryItem
    fields = ['image']


class EditFaqGallery(UpdateWithInlinesView):
    success_url = "/faq/"
    template_name = "entries/faq/edit.html"
    model = Gallery
    inlines = [ImageFaqInline]
    fields = '__all__'


class DeleteFaq(DeleteView):
    success_url = "/faq/"
    template_name = "entries/faq/delete.html"
    model = Gallery
