from django.contrib import admin

from .models import News, NewsCategory, Article, ArticleCategory, File, FileCategory, Game, \
    Author, ModCategory, Mod, ImageGalleryCategory, ImageGallery, Guide, FaqCategory, Faq


# ////--------
# NEWS: НОВОСТИ
# ////--------


@admin.register(NewsCategory)
class CategoriesNewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'author', 'categories', 'short_descript',
              'descript', 'image', 'objgallery', 'in_top', 'at_main', 'source', 'tags']
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


@admin.register(ArticleCategory)
class CategoriesArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'author', 'categories', 'short_descript',
              'descript', 'image', 'objgallery', 'in_top', 'at_main', 'source', 'tags']
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


@admin.register(FileCategory)
class CategoriesFilesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


@admin.register(File)
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


@admin.register(Game)
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
class GuideItemInline(admin.StackedInline):
    model = Guide


@admin.register(ModCategory)
class CategoriesModsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


@admin.register(Mod)
class ModAdmin(admin.ModelAdmin):
    inlines = [GuideItemInline]
    list_display = ['id', 'file', 'categories']
    search_fields = ['id', 'file', 'categories']
    list_filter = ('id', 'file', 'categories')


# /////////////---------------------
# IMAGEgALLERY: ГАЛЕРЕЯ ИЗОБРАЖЕНИЙ
# /////////////---------------------


@admin.register(ImageGalleryCategory)
class CategoriesImagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'categories', 'tag_list']
    search_fields = ['title', 'slug', 'tags']
    list_filter = ('categories', 'datetime', 'tags')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


# ///////----------------------
# GUIDES: ГАЙДЫ ПО ПРОХОЖДЕНИЮ
# ///////----------------------


@admin.register(Guide)
class GuidesAdmin(admin.ModelAdmin):
    list_display = ['name', 'mod', 'type0f']
    search_fields = ['name', 'mod']
    list_filter = ('name', 'mod', 'type0f')


# ////--------------------------
# FAQ: ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ
# ////--------------------------


@admin.register(FaqCategory)
class CategoriesModsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


@admin.register(Faq)
class ModAdmin(admin.ModelAdmin):
    list_display = ['question', 'id', 'category']
    search_fields = ['question', 'id', 'category']
    list_filter = ('question', 'datetime', 'author', 'category')
