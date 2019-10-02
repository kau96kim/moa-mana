from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models
from api.mana.models import Mana, Episode


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manas = models.ManyToManyField(Mana)
    episodes = models.ManyToManyField(Episode)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
