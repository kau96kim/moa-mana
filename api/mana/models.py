from django.db import models
from api.models import Url


class Mana(models.Model):
    title = models.CharField(max_length=100, unique=True)
    link = models.URLField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_link(self):
        url = Url.objects.get(id=1).link
        link = url + self.link

        return link
