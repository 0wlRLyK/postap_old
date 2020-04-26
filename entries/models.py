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
    return '/'.join(['entries', 'gallery', str(instance.slug), str(instance.pk), filename])


class Gallery(models.Model):
    id = models.AutoField(primary_key=True)

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

    def save(self, *args, **kwargs):
        if self.id is None:
            # saved_image1, saved_image2, saved_image3, saved_image4, saved_image5, saved_image6, saved_image7, saved_image8, saved_image9, saved_image10, saved_image11, saved_image12, saved_image13, saved_image14, saved_image15 = self.image1, self.image2, self.image3, self.image4, self.image5, self.image6,self.image7, self.image8, self.image9, self.image10, self.image11, self.image12, self.image13, self.image14, self.image15
            # saved_image1 = saved_image2 = saved_image3 = saved_image4 = saved_image5 = saved_image6 = saved_image7 = saved_image8 = saved_image9 = saved_image10 = saved_image11 = saved_image12 = saved_image13 = saved_image14 = saved_image15 = None
            # super(Gallery, self).save(*args, **kwargs)
            # self.image1, self.image2, self.image3, self.image4, self.image5, self.image6,self.image7, self.image8, self.image9, self.image10, self.image11, self.image12, self.image13, self.image14, self.image15 = saved_image1, saved_image2, saved_image3, saved_image4, saved_image5, saved_image6, saved_image7, saved_image8, saved_image9, saved_image10, saved_image11, saved_image12, saved_image13, saved_image14, saved_image15
            saved_image1 = self.image1
            self.image1 = None
            super(Gallery, self).save(*args, **kwargs)
            self.image1 = saved_image1
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(Gallery, self).save(*args, **kwargs)


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
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=True, null=True)
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
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=True, null=True)
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
