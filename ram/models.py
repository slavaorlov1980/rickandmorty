from django.db import models


class AllChars(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    status = models.CharField(max_length=50, blank=True, verbose_name='Статус')
    species = models.CharField(max_length=50, blank=True, verbose_name='Вид')
    type = models.CharField(max_length=50, blank=True, verbose_name='Тип')
    gender = models.CharField(max_length=20, blank=True, verbose_name='Пол')
    origin = models.JSONField(blank=True, verbose_name='Происхождение')
    location = models.JSONField(blank=True, verbose_name='Место обитания')
    image = models.ImageField(blank=True, verbose_name='Изображение')
    url = models.URLField(blank=True, verbose_name='URL адрес')
    created = models.DateTimeField(blank=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'
        ordering = ['id']


class Episodes(models.Model):
    id = models.IntegerField(primary_key=True)
    episode = models.CharField(max_length=250, verbose_name='Эпизод')
    chars = models.ManyToManyField(AllChars)

    def __str__(self):
        return self.episode

    class Meta:
        verbose_name = 'Эпизод'
        verbose_name_plural = 'Эпизоды'
        ordering = ['episode']

