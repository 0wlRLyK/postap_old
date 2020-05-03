from django.db import models


def upload_to(instance, filename):
    return '/'.join(['gallery', str(instance.entry.slug), str(instance.entry.pk), filename])


class GalleryItem(models.Model):
    image = models.ImageField(upload_to=upload_to)
    entry = models.ForeignKey('Gallery', null=True, on_delete=models.CASCADE, related_name="image")

    # def save(self, *args, **kwargs):
    #     if self.id is None:
    #         saved_image = self.image
    #         self.image = None
    #         super(Gallery, self).save(*args, **kwargs)
    #         self.image = saved_image
    #         if 'force_insert' in kwargs:
    #             kwargs.pop('force_insert')
    #
    #     super(Gallery, self).save(*args, **kwargs)


class Gallery(models.Model):
    name = models.CharField(max_length=200, )
    slug = models.SlugField(max_length=50, null=True)
