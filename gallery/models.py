from django.db import models
from stdimage import StdImageField


def upload_to(instance, filename):
    return '/'.join(['gallery', str(instance.entry.slug), str(instance.entry.pk), filename])


class GalleryItem(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок", default="", blank=True)
    descript = models.CharField(max_length=1000, verbose_name="Короткое описание", default="", blank=True)
    image = StdImageField(upload_to=upload_to, null=True, blank=True,
                          variations={'thumbnail': (120, 90), 'small': (300, 225),
                                      'middle': (600, 450), 'big': (800, 600), })
    entry = models.ForeignKey('Gallery', null=True, on_delete=models.CASCADE, related_name="image")


class Gallery(models.Model):
    name = models.CharField(max_length=200, )
    slug = models.SlugField(max_length=50, null=True)