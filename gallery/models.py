from django.db import models
from stdimage import StdImageField


def upload_to(instance, filename):
    return '/'.join(['gallery', str(instance.entry.slug), str(instance.entry.pk), filename])


class GalleryItem(models.Model):
    image = StdImageField(upload_to=upload_to,
                          variations={'thumbnail': (120, 90), 'small': (300, 225),
                                      'middle': (600, 450), 'big': (800, 600), })
    entry = models.ForeignKey('Gallery', null=True, on_delete=models.CASCADE, related_name="image")


class Gallery(models.Model):
    name = models.CharField(max_length=200, )
    slug = models.SlugField(max_length=50, null=True)
