from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Tags(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название тега")


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


class Entry(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=25, help_text="Навзание, которое будет отображаться в URL", unique=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Автор")
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
    descript = HTMLField(verbose_name="Описание")
    tags = models.ManyToManyField(Tags, blank=True, verbose_name="Теги")
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


class CategoriesNews(Categories):
    pass

    class Meta:
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"


class EntryNews(ContentGalleryMixin, Entry):
    categories = models.ForeignKey(CategoriesNews, on_delete=models.DO_NOTHING, verbose_name="Категория", null=True)
    shortDescript = models.TextField(verbose_name="Короткое описание")
    source = models.URLField(blank=True, verbose_name="Источник")
    image = models.ImageField(upload_to='entries/categories', default='spostap.png', null=True, unique=False,
                              verbose_name="Илюстрация")
    gallery = models.FileField(upload_to='entries/news', blank=True, null=True)
	
	
	def get_image_filename(instance, filename):
	    title = instance.post.title
	    slug = slugify(title)
	    return "post_images/%s-%s" % (slug, filename) 

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
		
class Images(models.Model):
    post = models.ForeignKey(Post, default=None)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')		
