from django.db import models
import json


class AllChars(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, blank=True)
    species = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    origin = models.JSONField(blank=True)
    location = models.JSONField(blank=True)
    image = models.ImageField(blank=True)
    url = models.URLField(blank=True)
    created = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name


class Episodes(models.Model):
    id = models.IntegerField(primary_key=True)
    episode = models.IntegerField()
    id_char = models.ManyToManyField(AllChars)

    def __str__(self):
        return self.episode


# class CharEpisodeLink(models.Model):
#     id_char = models.IntegerField()
#     id_episode = models.IntegerField()

