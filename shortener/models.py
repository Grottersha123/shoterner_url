from django.db import models
from .utils import create_shortcode

from django.conf import settings


# Create your models here.

class AnimeUrlManger(models.Model):
    def all(self, *args, **kwargs):
        qs = super(AnimeUrl, self).all(*args, **kwargs)
        return qs.filter(active=True)

    def refresh_codes(self):
        qs = AnimeUrl.objects.filter(id__gte=1)
        count_codes = 0
        for q in qs:
            q.short_code = create_shortcode(q)
            print(q.short_code)
            q.save()
            count_codes += 1
        return 'New {} - codes'.format(count_codes)


class AnimeUrl(models.Model):
    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    url = models.CharField(max_length=255, verbose_name='Ссылка')
    short_code = models.CharField(max_length=settings.SHORTCODE_MAX, unique=True, blank=True, verbose_name='Код ссылки')
    updated = models.DateField(auto_now=True)
    timestamp = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    object = AnimeUrlManger()

    def save(self, *args, **kwargs):
        if self.short_code is None or self.short_code == "":
            self.short_code = create_shortcode(self)
        super(AnimeUrl, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.url
