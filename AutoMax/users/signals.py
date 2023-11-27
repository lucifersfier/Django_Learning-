from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#now i am going to be creating a function which is basically going to run when our user gets creates or when a signal basically gets made.
from .models import Profile
@receiver(post_save, sender=User)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
     