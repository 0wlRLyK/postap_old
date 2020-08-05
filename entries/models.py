from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import FileExtensionValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.text import slugify
from favorites.models import LikeDislike
from gallery.models import Gallery
from hitcount.models import HitCountMixin, HitCount
from kp_html_meta.models import KPMetaHelper
from stdimage import StdImageField
from taggit.managers import TaggableManager


def upload_to_entries(instance, filename):
    return '/'.join(['entries', str(instance.module_name), str(instance.pk), filename])


# ------------
# ABSTRACT CLASSES
# ------------

class EntryBase(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=25, help_text="Навзание, которое будет отображаться в URL", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class EntryDescr(EntryBase):
    descript = RichTextUploadingField(verbose_name="Описание")

    class Meta:
        abstract = True


class EntryAuthor(EntryBase):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Автор")

    class Meta:
        abstract = True


class EntryFull(EntryAuthor, HitCountMixin, KPMetaHelper):
    module_name = None
    publ_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления материала")
    short_descript = RichTextUploadingField(verbose_name="Короткое описание")
    descript = RichTextUploadingField(verbose_name="Описание")
    tags = TaggableManager(blank=True)
    image = StdImageField(upload_to=upload_to_entries, default='postap.png', null=True, unique=False,
                          verbose_name="Илюстрация",
                          variations={'thumbnail': (120, 90), 'small': (300, 225), 'middle': (600, 450),
                                      'big': (800, 600), })
    objgallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=True, null=True, default=None)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')
    votes = GenericRelation(LikeDislike, related_query_name=module_name)

    class Meta:
        abstract = True

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse(f'entries_app:{self.module_name}_details', kwargs={'slug': self.slug})

    def get_kp_meta_title(self):
        return self.title

    def get_kp_meta_description(self):
        return self.short_descript[:160]

    def get_kp_meta_keywords(self):
        return None

    def get_kp_meta_graph_type(self):
        return None

    def get_kp_meta_graph_image(self):
        return self.image

    def get_kp_meta_graph_url(self):
        return None

    def get_kp_meta_graph_locale(self):
        return None

    def get_kp_meta_graph_site_name(self):
        return None

    def get_kp_get_base_url(self):
        return None


class EntryFullMain(EntryFull):
    in_top = models.BooleanField(default=False, verbose_name="Закрепить материал", blank="True")
    at_main = models.BooleanField(default=False, verbose_name="Вывести материал на главную страницу", blank="True")
    posted = models.BooleanField(default=True, verbose_name="Материал опубликован")

    class Meta:
        abstract = True


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, verbose_name="Название категории")
    slug = models.CharField(max_length=25, help_text="Навзание, которое будет отображаться в URL", unique=True)
    descript = RichTextUploadingField(verbose_name="Описание")
    image = StdImageField(upload_to='entries', default='postap.png', verbose_name="Изображение", blank=True,
                          variations={'thumbnail': (120, 90), 'small': (300, 225), 'middle': (600, 450),
                                      'big': (800, 600), })
    icon = models.FileField(upload_to='entries/categories', default='postap.png',
                            validators=[FileExtensionValidator(['png', 'gif', 'svg'])],
                            verbose_name="Иконка категории", help_text="Форматы svg, png, gif", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


# ------------
# START-of-MODULES
# ------------
# ////--------
# NEWS: НОВОСТИ
# ////--------


class NewsCategory(Category):
    pass

    class Meta:
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"


class News(EntryFullMain):
    module_name = "news"

    categories = models.ForeignKey(NewsCategory, on_delete=models.DO_NOTHING, verbose_name="Категория", null=True)
    source = models.URLField(blank=True, verbose_name="Источник")

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        if self.id is None:
            saved_image = self.image
            self.image = None
            super(News, self).save(*args, **kwargs)
            self.image = saved_image
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(News, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


# /////////-------
# ARTICLES: СТАТЬИ
# /////////-------

class ArticleCategory(Category):
    pass

    class Meta:
        verbose_name = "Категория статей"
        verbose_name_plural = "Категории статей"


class Article(EntryFullMain):
    module_name = "article"

    categories = models.ForeignKey(ArticleCategory, on_delete=models.DO_NOTHING, verbose_name="Категория", null=True)
    source = models.URLField(blank=True, verbose_name="Источник")

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        if self.id is None:
            saved_image = self.image
            self.image = None
            super(Article, self).save(*args, **kwargs)
            self.image = saved_image
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(Article, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


# //////-------
# FILES: ФАЙЛЫ
# //////-------

class FileCategory(Category):
    pass

    class Meta:
        verbose_name = "Категория файлов"
        verbose_name_plural = "Категории файлов"


def upload_to_torrent(instance, filename):
    return '/'.join(['entries', 'files', str(instance.pk), filename])


def upload_to_file(instance, filename):
    return '/'.join(['entries', 'files', 'torrent', str(instance.pk), filename])


class File(EntryFullMain):
    module_name = "file"

    categories = models.ForeignKey(FileCategory, on_delete=models.DO_NOTHING, verbose_name="Категория", null=True)

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

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        if self.id is None:
            saved_image, saved_file, saved_tor1, saved_tor2, saved_tor3 = self.image, self.file, self.torrent1, self.torrent2, self.torrent3
            self.image, self.file, self.torrent1, self.torrent2, self.torrent3 = None, None, None, None, None
            super(File, self).save(*args, **kwargs)
            self.image, self.file, self.torrent1, self.torrent2, self.torrent3 = saved_image, saved_file, saved_tor1, saved_tor2, saved_tor3
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(File, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"


# //////-------
# GAME: ИГРЫ
# //////-------

def upload_to_games(instance, filename):
    return '/'.join(['games', str(instance.slug), filename])


class Game(EntryDescr):
    module_name = "game"

    bg = models.ImageField(upload_to=upload_to_games, verbose_name="Фоновое изображение")
    image = StdImageField(upload_to=upload_to_games, verbose_name="Обложка игры",
                          variations={'thumbnail': (120, 90), 'small': (300, 225), 'middle': (600, 450),
                                      'big': (800, 600), 'thumbnail_sq': (120, 90, True), 'small_sq': (300, 225, True),
                                      'middle_sq': (600, 450, True),
                                      'big_sq': (800, 600, True)})
    logo = models.FileField(upload_to=upload_to_games,
                            validators=[FileExtensionValidator(['png', 'gif', 'svg'])],
                            verbose_name="Логотип игры", help_text="Форматы svg, png, gif", blank=True)
    release_date = models.DateField(verbose_name="Дата релиза", blank=True)
    features = RichTextUploadingField(blank=True)
    requirements = RichTextUploadingField(blank=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        if self.id is None:
            saved_image, saved_bg, saved_bg = self.image, self.bg, self.logo
            self.image, self.bg, self.logo = None, None, None
            super(Game, self).save(*args, **kwargs)
            self.image, self.bg, self.logo = saved_image, saved_bg, saved_bg
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(Game, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"


# ////////--------
# AUTHOR: АВТОРЫ
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
    bio = RichTextUploadingField()
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


class ModCategory(Category):
    pass

    class Meta:
        verbose_name = "Категория модов"
        verbose_name_plural = "Категории модов"


class Mod(EntryBase, HitCountMixin, KPMetaHelper):
    module_name = "mod"

    categories = models.ForeignKey(ModCategory, on_delete=models.DO_NOTHING, verbose_name="Категория модов")
    gameobj = models.ForeignKey(Game, on_delete=models.DO_NOTHING, verbose_name="Модифицируемая игра", default=None,
                                blank=False)
    file = models.ForeignKey(File, on_delete=models.DO_NOTHING, verbose_name="Файл")
    plot = RichTextUploadingField(blank=True, verbose_name="Коротко о сюжете")
    features = RichTextUploadingField(blank=True, verbose_name="Особенности")
    innovations = RichTextUploadingField(blank=True, verbose_name="Нововведения")
    gameplay = RichTextUploadingField(blank=True, verbose_name="Гемйплей")
    locations = RichTextUploadingField(blank=True, verbose_name="Локации")
    weapons = RichTextUploadingField(blank=True, verbose_name="Другое")
    other = RichTextUploadingField(blank=True, verbose_name="Другие особенности и нововведения модификации")
    author = models.ForeignKey(Author, null=True, blank=True, default=None, on_delete=models.DO_NOTHING,
                               verbose_name="Автор модификации")

    class Meta:
        verbose_name = "Мод"
        verbose_name_plural = "Моды"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse(f'entries_app:{self.module_name}_details', kwargs={'slug': self.slug})

    def get_kp_meta_title(self):
        return self.title

    def get_kp_meta_description(self):
        return self.descript[:160]

    def get_kp_meta_keywords(self):
        return None

    def get_kp_meta_graph_type(self):
        return None

    def get_kp_meta_graph_image(self):
        return self.image

    def get_kp_meta_graph_url(self):
        return None

    def get_kp_meta_graph_locale(self):
        return None

    def get_kp_meta_graph_site_name(self):
        return None

    def get_kp_get_base_url(self):
        return None


# /////////////---------------------
# IMAGEgALLERY: ГАЛЕРЕЯ ИЗОБРАЖЕНИЙ
# /////////////---------------------


class ImageGalleryCategory(Category):
    pass

    class Meta:
        verbose_name = "Категория галереи"
        verbose_name_plural = "Категории галереи"


class ImageGallery(EntryFullMain):
    module_name = "gallery"

    categories = models.ForeignKey(ImageGalleryCategory, on_delete=models.DO_NOTHING, verbose_name="Категория",
                                   null=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        if self.id is None:
            saved_image = self.image
            self.image = None
            super(ImageGallery, self).save(*args, **kwargs)
            self.image = saved_image
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(ImageGallery, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


# ///////----------------------
# GUIDES: ГАЙДЫ ПО ПРОХОЖДЕНИЮ
# ///////----------------------

class Guide(models.Model):
    TYPE_OF_GUIDE = (
        ("main", "Сюжетный квест"),
        ("side", "Побочный квест"),
        ("additional", "Дополнительный"),
        ("items", "Метонахождение квестовых предметов"),
        ("tools", "Метонахождение инстурментов"),
        ("interesting", "Интересности"),
        ("easter_eggs", "Пасхалки"),
        ("other", "Другое"),
    )
    mod = models.ForeignKey(Mod, on_delete=models.DO_NOTHING, verbose_name="Модификация", related_name="modguides")
    name = models.CharField(max_length=300, verbose_name="Навзание квеста")
    type0f = models.CharField(max_length=100, choices=TYPE_OF_GUIDE, verbose_name="Тип гайда")
    descript = RichTextUploadingField(verbose_name="Описание квеста")
    solution = RichTextUploadingField(verbose_name="Решение квеста")
    votes = GenericRelation(LikeDislike, related_query_name='guides')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Гайд по прохождению"
        verbose_name_plural = "Гайды по прохождению"


# ////--------------------------
# FAQ: ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ
# ////--------------------------


class FaqCategory(Category):
    pass

    class Meta:
        verbose_name = "Категория FAQ"
        verbose_name_plural = "Категории FAQ"


class Faq(models.Model):
    question = models.CharField(max_length=400, verbose_name="Вопрос")
    category = models.ForeignKey(FaqCategory, on_delete=models.DO_NOTHING, verbose_name="Категория")
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Автор")
    publ_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
    question_descript = RichTextUploadingField(verbose_name="Описание вопроса", blank=True)
    answer = RichTextUploadingField(verbose_name="Описание ответа", blank=True)
    objgallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=True, null=True, default=None)

    posted = models.BooleanField(default=True, verbose_name="Материал опубликован")
    votes = GenericRelation(LikeDislike, related_query_name='faqs')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Часто задаваемые вопросы"
