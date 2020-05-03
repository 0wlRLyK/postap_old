from django.contrib import admin

from .models import EntryNews, CategoriesNews, EntryArticle, CategoriesArticle, EntryFile, CategoriesFiles


# ////--------
# NEWS: НОВОСТИ
# ////--------


@admin.register(CategoriesNews)
class CategoriesNewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


@admin.register(EntryNews)
class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'author', 'categories', 'shortDescript',
              'descript', 'image', 'objgallery', 'inTop', 'atMain', 'source', 'tags']
    list_display = ['title', 'categories', 'tag_list']
    search_fields = ['title', 'slug', 'tags']
    list_filter = ('categories', 'datetime', 'tags')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


# /////////-------
# ARTICLES: СТАТЬИ
# /////////-------


@admin.register(CategoriesArticle)
class CategoriesArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


@admin.register(EntryArticle)
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'author', 'categories', 'shortDescript',
              'descript', 'image', 'objgallery', 'inTop', 'atMain', 'source', 'tags']
    list_display = ['title', 'categories', 'tag_list']
    search_fields = ['title', 'slug', 'tags']
    list_filter = ('categories', 'datetime', 'tags')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


# //////-------
# FILES: ФАЙЛЫ
# //////-------


@admin.register(CategoriesFiles)
class CategoriesFilesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


@admin.register(EntryFile)
class FileAdmin(admin.ModelAdmin):
    list_display = ['title', 'categories', 'tag_list']
    search_fields = ['title', 'slug', 'tags']
    list_filter = ('categories', 'datetime', 'tags')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
