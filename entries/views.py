from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView

from .forms import NewsAddForm
from .models import EntryNews, Gallery
from .variables import NEWS


class HomePage(TemplateView):
    template_name = 'temporary/home.html'
    extra_context = {
        "newsEntries": EntryNews.objects.filter(atMain=True, )[:5],
        "newsURL": NEWS.module_list(),
    }


# NEWS

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
        gallery.slug = "{0}{1}".format("news", gallery.entry_id)
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
