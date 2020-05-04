from django.contrib import admin

from .models import EntryNews, CategoriesNews, EntryArticle, CategoriesArticle, EntryFile, CategoriesFiles, Games, \
    Author, CategoriesMods, EntryMod, CategoriesImages, EntryImageGallery


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


# //////-------
# GAMES: ИГРЫ
# //////-------


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    search_fields = ['title', 'slug']


# ////////--------
# AUTHORS: АВТОРЫ
# ////////--------

@admin.register(Author)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'nickname']
    search_fields = ['name', 'nickname']


# //////-----
# MODS: МОДЫ
# //////-----


@admin.register(CategoriesMods)
class CategoriesModsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


@admin.register(EntryMod)
class ModAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'categories']
    search_fields = ['id', 'file', 'categories']
    list_filter = ('id', 'file', 'categories')


# /////////////---------------------
# IMAGEgALLERY: ГАЛЕРЕЯ ИЗОБРАЖЕНИЙ
# /////////////---------------------


@admin.register(CategoriesImages)
class CategoriesImagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


@admin.register(EntryImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'categories', 'tag_list']
    search_fields = ['title', 'slug', 'tags']
    list_filter = ('categories', 'datetime', 'tags')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
