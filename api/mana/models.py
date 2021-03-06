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


class Episode(models.Model):
    DOWNLOAD_STATUS = [
        ('X', 'Not downloaded'),
        ('!', 'Downloading'),
        ('O', 'Downloaded')
    ]

    mana = models.ForeignKey(Mana, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField()
    link = models.URLField()
    status = models.CharField(max_length=1,
                              choices=DOWNLOAD_STATUS,
                              default='X')

    def __str__(self):
        return self.title

    def get_link(self):
        url = Url.objects.get(id=1).link
        link = url + self.link

        return link
