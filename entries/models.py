from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.validators import FileExtensionValidator
from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from tinymce.models import HTMLField


class Tags(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название тега")


def upload_to(instance, filename):
    return '/'.join(['entries', 'gallery', str(instance.slug), filename])


class Gallery(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название", blank=True)
    entry = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, blank=True, null=True)
    slug = models.SlugField(max_length=50, default="none")
    image1 = models.ImageField(upload_to=upload_to, blank=True)
    image2 = models.ImageField(upload_to=upload_to, blank=True)
    image3 = models.ImageField(upload_to=upload_to, blank=True)
    image4 = models.ImageField(upload_to=upload_to, blank=True)
    image5 = models.ImageField(upload_to=upload_to, blank=True)
    image6 = models.ImageField(upload_to=upload_to, blank=True)
    image7 = models.ImageField(upload_to=upload_to, blank=True)
    image8 = models.ImageField(upload_to=upload_to, blank=True)
    image9 = models.ImageField(upload_to=upload_to, blank=True)
    image10 = models.ImageField(upload_to=upload_to, blank=True)
    image11 = models.ImageField(upload_to=upload_to, blank=True)
    image12 = models.ImageField(upload_to=upload_to, blank=True)
    image13 = models.ImageField(upload_to=upload_to, blank=True)
    image14 = models.ImageField(upload_to=upload_to, blank=True)
    image15 = models.ImageField(upload_to=upload_to, blank=True)

    def __str__(self):
        if self.entry:
            return "{0} - {1}".format(self.entry.name, self.title)
        return "none - {0}".format(self.title)


class Categories(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название категории")
    slug = models.CharField(max_length=25, help_text="Навзание, которое будет отображаться в URL", unique=True)
    descript = HTMLField(verbose_name="Описание")
    image = models.ImageField(upload_to='entries', default='postap.png', verbose_name="Изображение", blank=True)
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


class Entry(models.Model):
    ModuleNAME = "none"

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=25, help_text="Навзание, которое будет отображаться в URL", unique=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Автор")
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
    descript = HTMLField(verbose_name="Описание")
    tags = TaggableManager(blank=True)
    image = models.ImageField(upload_to=upload_to_entries, default='postap.png', null=True, unique=False,
                              verbose_name="Илюстрация")
    inTop = models.BooleanField(default=False, verbose_name="Закрепить материал", blank="True")
    atMain = models.BooleanField(default=False, verbose_name="Вывести материал на главную страницу", blank="True")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


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


class EntryNews(Entry):
    ModuleNAME = "news"

    categories = models.ForeignKey(CategoriesNews, on_delete=models.DO_NOTHING, verbose_name="Категория", null=True)
    shortDescript = HTMLField(verbose_name="Короткое описание")
    source = models.URLField(blank=True, verbose_name="Источник")
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


# /////////-------
# ARTICLES: СТАТЬИ
# /////////-------

class CategoriesArticles(Categories):
    pass

    class Meta:
        verbose_name = "Категория cтатей"
        verbose_name_plural = "Категории статей"
