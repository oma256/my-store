from django.db import models

from utils.upload_image import upload_instance_image


class Movie(models.Model):
    name = models.CharField(verbose_name='Название', max_length=256)
    description = models.TextField(verbose_name='Описание')
    rating = models.PositiveSmallIntegerField(verbose_name='Оценка')
    release_date = models.DateField(verbose_name='Дата выхода')
    genres = models.ManyToManyField('Genre', related_name='genres')
    image = models.ImageField(verbose_name='Изображение',
                              upload_to=upload_instance_image)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

