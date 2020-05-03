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
                          variations={'thumbnail_sq': (100, 100), 'thumbnail': (120, 90),
                                      'thumbnail_sq_crp': (100, 100, True), 'thumbnail_crp': (120, 90, True),
                                      'small_sq': (200, 200), 'small': (200, 150), 'small_sq_crp': (200, 200, True),
                                      'small_crp': (200, 150, True), 'medium_sq': (350, 350), 'medium': (320, 240),
                                      'medium_sq_crp': (350, 350, True), 'medium_crp': (320, 240, True),
                                      'large_sq': (600, 600), 'large': (600, 450), 'large_sq_crp': (600, 600, True),
                                      'large_crp': (600, 450, True), 'res800x600': (800, 600),
                                      'res800x600_crp': (800, 800, True), 'res1024x600': (1024, 600),
                                      'res1024x600_crp': (1024, 600, True), 'res1280x720': (1280, 720),
                                      'res1280x720_crp': (1280, 720, True), 'res1440x1080': (1440, 1080),
                                      'res1440x1080_crp': (1440, 1080, True), 'res1920x1080': (1920, 1080),
                                      'res1920x1080_crp': (1920, 1080, True), '4k': (3840, 2160),
                                      '4k_crp': (3840, 2160, True), }, )
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
    objgallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=True, null=True)
    tags = TaggableManager(blank=True)
    image = StdImageField(upload_to=upload_to_entries, default='postap.png', null=True, unique=False,
                          verbose_name="Илюстрация",
                          variations={'thumbnail_sq': (100, 100), 'thumbnail': (120, 90),
                                      'thumbnail_sq_crp': (100, 100, True), 'thumbnail_crp': (120, 90, True),
                                      'small_sq': (200, 200), 'small': (200, 150), 'small_sq_crp': (200, 200, True),
                                      'small_crp': (200, 150, True), 'medium_sq': (350, 350), 'medium': (320, 240),
                                      'medium_sq_crp': (350, 350, True), 'medium_crp': (320, 240, True),
                                      'large_sq': (600, 600), 'large': (600, 450), 'large_sq_crp': (600, 600, True),
                                      'large_crp': (600, 450, True), 'res800x600': (800, 600),
                                      'res800x600_crp': (800, 800, True), 'res1024x600': (1024, 600),
                                      'res1024x600_crp': (1024, 600, True), 'res1280x720': (1280, 720),
                                      'res1280x720_crp': (1280, 720, True), 'res1440x1080': (1440, 1080),
                                      'res1440x1080_crp': (1440, 1080, True), 'res1920x1080': (1920, 1080),
                                      'res1920x1080_crp': (1920, 1080, True), '4k': (3840, 2160),
                                      '4k_crp': (3840, 2160, True), }, )
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
    descript = HTMLField(verbose_name="Описание")
    shortDescript = HTMLField(verbose_name="Короткое описание")
    source = models.URLField(blank=True, verbose_name="Источник")
    objgallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=True, null=True)
    tags = TaggableManager(blank=True)
    image = StdImageField(upload_to=upload_to_entries, default='postap.png', null=True, unique=False,
                          verbose_name="Илюстрация",
                          variations={'thumbnail_sq': (100, 100), 'thumbnail': (120, 90),
                                      'thumbnail_sq_crp': (100, 100, True), 'thumbnail_crp': (120, 90, True),
                                      'small_sq': (200, 200), 'small': (200, 150), 'small_sq_crp': (200, 200, True),
                                      'small_crp': (200, 150, True), 'medium_sq': (350, 350), 'medium': (320, 240),
                                      'medium_sq_crp': (350, 350, True), 'medium_crp': (320, 240, True),
                                      'large_sq': (600, 600), 'large': (600, 450), 'large_sq_crp': (600, 600, True),
                                      'large_crp': (600, 450, True), 'res800x600': (800, 600),
                                      'res800x600_crp': (800, 800, True), 'res1024x600': (1024, 600),
                                      'res1024x600_crp': (1024, 600, True), 'res1280x720': (1280, 720),
                                      'res1280x720_crp': (1280, 720, True), 'res1440x1080': (1440, 1080),
                                      'res1440x1080_crp': (1440, 1080, True), 'res1920x1080': (1920, 1080),
                                      'res1920x1080_crp': (1920, 1080, True), '4k': (3840, 2160),
                                      '4k_crp': (3840, 2160, True), }, )
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
