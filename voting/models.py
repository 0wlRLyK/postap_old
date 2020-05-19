from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.text import slugify
from entries.models import EntryMod
from stdimage import StdImageField


# ------------
# //////--------.........
# BASE: БАЗОВЫЕ КЛАССЫ
# //////--------.,.,.,.,.


class CategoriesBase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, verbose_name="Название категории")
    slug = models.CharField(max_length=25, help_text="Навзание, которое будет отображаться в URL", unique=True)
    descript = RichTextUploadingField(verbose_name="Описание")
    image = StdImageField(upload_to='voting/categories', default='postap.png', verbose_name="Изображение", blank=True,
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

    class Meta:
        abstract = True


class PollBase(models.Model):
    title = models.CharField(max_length=200)
    descript = RichTextUploadingField(verbose_name="Описание")
    category = models.ForeignKey(CategoriesBase, on_delete=models.DO_NOTHING, verbose_name="Категория")
    image = StdImageField(upload_to='entries', default='postap.png', verbose_name="Изображение", blank=True,
                          variations={'thumbnail': (120, 90), 'small': (300, 225), 'middle': (600, 450),
                                      'big': (800, 600), })
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class ChoiceBase(models.Model):
    question = models.ForeignKey('self', on_delete=models.CASCADE)
    choice_title = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_title

    class Meta:
        abstract = True


# //////--------
# POLLS: ОПРОСЫ
# //////--------
class PollCategories(CategoriesBase):
    pass

    class Meta:
        verbose_name = "Категория опросов"
        verbose_name_plural = "Категории опросов"


class Poll(PollBase):
    category = models.ForeignKey(PollCategories, on_delete=models.DO_NOTHING, verbose_name="Категория")

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class Choice(ChoiceBase):
    question = models.ForeignKey(Poll, on_delete=models.CASCADE)
    image = StdImageField(upload_to='entries', default='postap.png', verbose_name="Изображение", blank=True,
                          variations={'thumbnail': (120, 90), 'small': (300, 225)})

    class Meta:
        verbose_name = "Вариант голосования"
        verbose_name_plural = "Варианты голосования"


# ////////////--------------------
# MOD VOTING: ГОЛОСОВАНИЕ ЗА МОДЫ
# ////////////--------------------


class ModVotingCategories(PollCategories):
    pass

    class Meta:
        verbose_name = "Категория выборов модификаций"
        verbose_name_plural = "Категории выборов модификаций"


class ModVoting(PollBase):
    category = models.ForeignKey(PollCategories, on_delete=models.DO_NOTHING, verbose_name="Категория")

    class Meta:
        verbose_name = "Выбор лучших модификаций"
        verbose_name_plural = "Выборы лучших модификаций"


class ModChoice(models.Model):
    question = models.ForeignKey(ModVoting, on_delete=models.CASCADE)
    mod = models.ForeignKey(EntryMod, on_delete=models.DO_NOTHING)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.mod.title


# ////////--------
# VOTING: ГОЛОСОВАНИЕ
# ////////--------


class VotingCategories(CategoriesBase):
    pass

    class Meta:
        verbose_name = "Категория голосований"
        verbose_name_plural = "Категории голосований"


class Voting(PollBase):
    category = models.ForeignKey(VotingCategories, on_delete=models.DO_NOTHING, verbose_name="Категория")

    class Meta:
        verbose_name = "Голосование"
        verbose_name_plural = "Голосования"


class Vote(ChoiceBase):
    question = models.ForeignKey(Voting, on_delete=models.CASCADE)
    image = StdImageField(upload_to='entries', default='postap.png', verbose_name="Изображение", blank=True,
                          variations={'thumbnail': (120, 90), 'small': (300, 225)})

    class Meta:
        verbose_name = "Вариант голосования"
        verbose_name_plural = "Варианты голосования"
