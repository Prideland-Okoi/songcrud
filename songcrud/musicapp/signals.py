from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Musiclover
from django.contrib.auth.models import User



@receiver(post_save, sender=User)
def create_musiclover(sender, instance, created, **kwargs):
    if created:
        Musiclover.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_musiclover(sender, instance, **kwargs):
    instance.musiclover.save()
