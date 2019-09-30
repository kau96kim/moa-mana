from django.db import models


class Url(models.Model):
    link = models.URLField()

    def __str__(self):
        return self.link
