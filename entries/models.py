from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.models import ContentType
from django.core.validators import FileExtensionValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.text import slugify
from gallery.models import Gallery
from stdimage import StdImageField
from taggit.managers import TaggableManager
from tinymce.models import HTMLField


# def upload_to(instance, filename):
#     return '/'.join(['entries', 'gallery', str(instance.slug), str(instance.pk), filename])
#
#
# class Gallery(models.Model):
#     id = models.AutoField(primary_key=True)
#
#     title = models.CharField(max_length=100, verbose_name="Название", blank=True)
#     entry = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, blank=True, null=True)
#     slug = models.SlugField(max_length=50, default="none")
#     image = models.ImageField(upload_to=upload_to, blank=True)
#
#     def __str__(self):
#         if self.entry:
#             return "{0} - {1}".format(self.entry.name, self.title)
#         return "none - {0}".format(self.title)
#
#     def save(self, *args, **kwargs):
#         if self.id is None:
#             saved_image = self.image
#             self.image = None
#             super(Gallery, self).save(*args, **kwargs)
#             self.image = saved_image
#             if 'force_insert' in kwargs:
#                 kwargs.pop('force_insert')
#
#         super(Gallery, self).save(*args, **kwargs)


class Categories(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название категории")
    slug = models.CharField(max_length=25, help_text="Навзание, которое будет отображаться в URL", unique=True)
    descript = HTMLField(verbose_name="Описание")
    image = StdImageField(upload_to='entries', default='postap.png', verbose_name="Изображение", blank=True,
                          variations={'thumbnail': (120, 90), 'small': (300, 225), 'middle': (600, 450),
                                      'big': (800, 600), })
    icon = models.FileField(upload_to='entries/categories',
                            validators=[FileExtensionValidator(['png', 'gif', 'svg'])],
                            verbose_name="Иконка категории", help_text="Форматы svg, png, gif", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


def upload_to_entries(instance, filename):
    return '/'.join(['entries', str(instance.ModuleNAME), str(instance.pk), filename])


# ------------
# START-of-MODULES
# ------------
# ////--------
# NEWS: НОВОСТИ
# ////--------


class CategoriesNews(Categories):
    pass

    class Meta:
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"


class EntryNews(models.Model):
    ModuleNAME = "news"

    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=25, help_text="Навзание, которое будет отображаться в URL", unique=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Автор")
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
    categories = models.ForeignKey(CategoriesNews, on_delete=models.DO_NOTHING, verbose_name="Категория", null=True)
    descript = HTMLField(verbose_name="Описание")
    shortDescript = HTMLField(verbose_name="Короткое описание")
    source = models.URLField(blank=True, verbose_name="Источник")
    objgallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=True, null=True, default=None)
    tags = TaggableManager(blank=True)
    image = StdImageField(upload_to=upload_to_entries, default='postap.png', null=True, unique=False,
                          verbose_name="Илюстрация",
                          variations={'thumbnail': (120, 90), 'small': (300, 225), 'middle': (600, 450),
                                      'big': (800, 600), })
    inTop = models.BooleanField(default=False, verbose_name="Закрепить материал", blank="True")
    atMain = models.BooleanField(default=False, verbose_name="Вывести материал на главную страницу", blank="True")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        if self.id is None:
            saved_image = self.image
            self.image = None
            super(EntryNews, self).save(*args, **kwargs)
            self.image = saved_image
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(EntryNews, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


# /////////-------
# ARTICLES: СТАТЬИ
# /////////-------

class CategoriesArticle(Categories):
    pass

    class Meta:
        verbose_name = "Категория статей"
        verbose_name_plural = "Категории статей"


class EntryArticle(models.Model):
    ModuleNAME = "articles"
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=25, help_text="Навзание, которое будет отображаться в URL", unique=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Автор")
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
    categories = models.ForeignKey(CategoriesArticle, on_delete=models.DO_NOTHING, verbose_name="Категория", null=True)
    shortDescript = HTMLField(verbose_name="Короткое описание")
    descript = HTMLField(verbose_name="Описание")
    image = StdImageField(upload_to=upload_to_entries, default='postap.png', null=True, unique=False,
                          verbose_name="Илюстрация",
                          variations={'thumbnail': (120, 90), 'small': (300, 225), 'middle': (600, 450),
                                      'big': (800, 600), })
    objgallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=True, null=True, default=None)
    source = models.URLField(blank=True, verbose_name="Источник")
    tags = TaggableManager(blank=True)
    inTop = models.BooleanField(default=False, verbose_name="Закрепить материал", blank="True")
    atMain = models.BooleanField(default=False, verbose_name="Вывести материал на главную страницу", blank="True")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        if self.id is None:
            saved_image = self.image
            self.image = None
            super(EntryArticle, self).save(*args, **kwargs)
            self.image = saved_image
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(EntryArticle, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


# //////-------
# FILES: ФАЙЛЫ
# //////-------

class CategoriesFiles(Categories):
    pass

    class Meta:
        verbose_name = "Категория файлов"
        verbose_name_plural = "Категории файлов"


def upload_to_torrent(instance, filename):
    return '/'.join(['entries', 'files', str(instance.pk), filename])


def upload_to_file(instance, filename):
    return '/'.join(['entries', 'files', 'torrent', str(instance.pk), filename])


class EntryFile(models.Model):
    ModuleNAME = "files"
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=25, help_text="Навзание, которое будет отображаться в URL", unique=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Автор")
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
    categories = models.ForeignKey(CategoriesFiles, on_delete=models.DO_NOTHING, verbose_name="Категория", null=True)
    shortDescript = HTMLField(verbose_name="Короткое описание")
    descript = HTMLField(verbose_name="Описание")
    image = StdImageField(upload_to=upload_to_entries, default='postap.png', null=True, unique=False,
                          verbose_name="Илюстрация",
                          variations={'thumbnail': (120, 90), 'small': (300, 225), 'middle': (600, 450),
                                      'big': (800, 600), })
    objgallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=True, null=True, default=None)
    file = models.FileField(upload_to=upload_to_file, verbose_name="Файл", blank=True)
    torrent1 = models.FileField(upload_to=upload_to_torrent,
                                validators=[FileExtensionValidator(['torrent'])],
                                verbose_name="Торрент #1", blank=True, )
    torrent2 = models.FileField(upload_to=upload_to_torrent,
                                validators=[FileExtensionValidator(['torrent'])],
                                verbose_name="Торрент #1", blank=True, )
    torrent3 = models.FileField(upload_to=upload_to_torrent,
                                validators=[FileExtensionValidator(['torrent'])],
                                verbose_name="Торрент #1", blank=True, )
    gdrive = models.URLField(blank=True, verbose_name="Google")
    yadrive = models.URLField(blank=True, verbose_name="Yandex")
    mega = models.URLField(blank=True, verbose_name="MEGA")
    source1 = models.URLField(blank=True, verbose_name="Другой источник #1")
    source2 = models.URLField(blank=True, verbose_name="Другой источник #2")
    source3 = models.URLField(blank=True, verbose_name="Другой источник #3")
    tags = TaggableManager(blank=True)
    inTop = models.BooleanField(default=False, verbose_name="Закрепить материал", blank="True")
    atMain = models.BooleanField(default=False, verbose_name="Вывести материал на главную страницу", blank="True")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        if self.id is None:
            saved_image, saved_file, saved_tor1, saved_tor2, saved_tor3 = self.image, self.file, self.torrent1, self.torrent2, self.torrent3
            self.image, self.file, self.torrent1, self.torrent2, self.torrent3 = None, None, None, None, None
            super(EntryFile, self).save(*args, **kwargs)
            self.image, self.file, self.torrent1, self.torrent2, self.torrent3 = saved_image, saved_file, saved_tor1, saved_tor2, saved_tor3
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(EntryFile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"


# //////-------
# GAMES: ИГРЫ
# //////-------

def upload_to_games(instance, filename):
    return '/'.join(['games', str(instance.slug), filename])


class Games(models.Model):
    ModuleNAME = "games"
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=250, verbose_name="Название игры")
    slug = models.SlugField(max_length=50, help_text="Навзание, которое будет отображаться в URL", unique=True)
    bg = models.ImageField(upload_to=upload_to_games, verbose_name="Фоновое изображение")
    image = StdImageField(upload_to=upload_to_games, verbose_name="Обложка игры",
                          variations={'thumbnail': (120, 90), 'small': (300, 225), 'middle': (600, 450),
                                      'big': (800, 600), 'thumbnail_sq': (120, 90, True), 'small_sq': (300, 225, True),
                                      'middle_sq': (600, 450, True),
                                      'big_sq': (800, 600, True)})
    logo = models.FileField(upload_to=upload_to_games,
                            validators=[FileExtensionValidator(['png', 'gif', 'svg'])],
                            verbose_name="Логотип игры", help_text="Форматы svg, png, gif", blank=True)
    descript = HTMLField()
    features = HTMLField(blank=True)
    requirements = HTMLField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        if self.id is None:
            saved_image, saved_bg, saved_bg = self.image, self.bg, self.logo
            self.image, self.bg, self.logo = None, None, None
            super(Games, self).save(*args, **kwargs)
            self.image, self.bg, self.logo = saved_image, saved_bg, saved_bg
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(Games, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"


# ////////--------
# AUTHORS: АВТОРЫ
# ////////--------

def upload_to_authors(instance, filename):
    return '/'.join(['entries', 'authors', str(instance.slug), filename])


class Author(models.Model):
    AUTHORdOMAIN = (
        ("youtuber", "Видео блогер"),
        ("bloger", "Блогер"),
        ("moder", "Мододел"),
        ("musician", "Музыкант"),
        ("painter", "Художник"),
        ("artist", "Творец"),
        ("writer", "Писатель"),
        ("unique_person", "Уникальная персона"),
    )
    name = models.CharField(max_length=200, verbose_name="Имя автора")
    slug = models.SlugField(max_length=50, help_text="Навзание, которое будет отображаться в URL", unique=True)
    nickname = models.CharField(max_length=200, verbose_name="Никнейм автора")
    bio = HTMLField()
    domain = models.CharField(choices=AUTHORdOMAIN, max_length=200, verbose_name="Сфера деятельности")
    avatar = StdImageField(upload_to=upload_to_authors, verbose_name="Аватар автора",
                           variations={'thumbnail': (50, 50), 'small': (100, 100), 'middle': (250, 250),
                                       'big': (500, 500)})
    bg = StdImageField(upload_to=upload_to_authors, verbose_name="Аватар автора", variations={'bg': (1900, 500, True)})
    vk = models.URLField(blank=True)
    discord = models.URLField(blank=True)
    tg = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    twitch = models.URLField(blank=True)
    artstation = models.URLField(blank=True)
    devianart = models.URLField(blank=True)
    site = models.URLField(blank=True)
    other1 = models.URLField(blank=True)
    other2 = models.URLField(blank=True)

    def __str__(self):
        return self.nickname

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.nickname)
        if self.id is None:
            saved_avatar, saved_bg = self.avatar, self.bg
            self.avatar, self.bg = None, None
            super(Author, self).save(*args, **kwargs)
            self.avatar, self.bg = saved_avatar, saved_bg
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(Author, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


# //////-----
# MODS: МОДЫ
# //////-----


class CategoriesMods(Categories):
    pass

    class Meta:
        verbose_name = "Категория модов"
        verbose_name_plural = "Категории модов"


class EntryMod(models.Model):
    ModuleNAME = "mods"
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=250, verbose_name="Название мода", default=None)
    slug = models.SlugField(max_length=50, help_text="Навзание, которое будет отображаться в URL", unique=True,
                            default=None)
    categories = models.ForeignKey(CategoriesMods, on_delete=models.DO_NOTHING, verbose_name="Категория модов")
    gameobj = models.ForeignKey(Games, on_delete=models.DO_NOTHING, verbose_name="Модифицируемая игра", default=None,
                                blank=False)
    file = models.ForeignKey(EntryFile, on_delete=models.DO_NOTHING, verbose_name="Файл")
    plot = HTMLField(blank=True, verbose_name="Коротко о сюжете")
    features = HTMLField(blank=True, verbose_name="Особенности")
    innovations = HTMLField(blank=True, verbose_name="Нововведения")
    gameplay = HTMLField(blank=True, verbose_name="Гемйплей")
    locations = HTMLField(blank=True, verbose_name="Локации")
    weapons = HTMLField(blank=True, verbose_name="Другое")
    other = HTMLField(blank=True, verbose_name="Другие особенности и нововведения модификации")
    author = models.ForeignKey(Author, null=True, blank=True, default=None, on_delete=models.DO_NOTHING,
                               verbose_name="Автор модификации")

    # guide = Guide

    class Meta:
        verbose_name = "Мод"
        verbose_name_plural = "Моды"
