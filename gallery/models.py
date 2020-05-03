from django.db import models
from stdimage import StdImageField


def upload_to(instance, filename):
    return '/'.join(['gallery', str(instance.entry.slug), str(instance.entry.pk), filename])


class GalleryItem(models.Model):
    image = StdImageField(upload_to=upload_to, variations={'thumbnail_sq': (100, 100), 'thumbnail': (120, 90),
                                                           'thumbnail_sq_crp': (100, 100, True),
                                                           'thumbnail_crp': (120, 90, True),
                                                           'small_sq': (200, 200), 'small': (200, 150),
                                                           'small_sq_crp': (200, 200, True),
                                                           'small_crp': (200, 150, True), 'medium_sq': (350, 350),
                                                           'medium': (320, 240),
                                                           'medium_sq_crp': (350, 350, True),
                                                           'medium_crp': (320, 240, True),
                                                           'large_sq': (600, 600), 'large': (600, 450),
                                                           'large_sq_crp': (600, 600, True),
                                                           'large_crp': (600, 450, True), 'res800x600': (800, 600),
                                                           'res800x600_crp': (800, 800, True),
                                                           'res1024x600': (1024, 600),
                                                           'res1024x600_crp': (1024, 600, True),
                                                           'res1280x720': (1280, 720),
                                                           'res1280x720_crp': (1280, 720, True),
                                                           'res1440x1080': (1440, 1080),
                                                           'res1440x1080_crp': (1440, 1080, True),
                                                           'res1920x1080': (1920, 1080),
                                                           'res1920x1080_crp': (1920, 1080, True), '4k': (3840, 2160),
                                                           '4k_crp': (3840, 2160, True), }, )
    entry = models.ForeignKey('Gallery', null=True, on_delete=models.CASCADE, related_name="image")


class Gallery(models.Model):
    name = models.CharField(max_length=200, )
    slug = models.SlugField(max_length=50, null=True)
