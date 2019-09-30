from django.db import models
from api.mana.models import Mana
from api.episode.models import Episode


class User(models.Model):
    nickname = models.CharField(max_length=10, unique=True)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=200)
    episodes = models.ManyToManyField(Episode)
    manas = models.ManyToManyField(Mana)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username
