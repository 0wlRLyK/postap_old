from django.db import models
from django.db.models import Sum


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

    def news(self):
        return self.get_queryset().filter(content_type__model='news').order_by('-news__pub_date')

    def article(self):
        return self.get_queryset().filter(content_type__model='article').order_by('-article__pub_date')

    def file(self):
        return self.get_queryset().filter(content_type__model='file').order_by('-article__pub_date')

    def gallery(self):
        return self.get_queryset().filter(content_type__model='imagegallery').order_by('-imagegallery__pub_date')

    def guide(self):
        return self.get_queryset().filter(content_type__model='guide').order_by('-guide__pub_date')

    def faq(self):
        return self.get_queryset().filter(content_type__model='faq').order_by('-faq__pub_date')
