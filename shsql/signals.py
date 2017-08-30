from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from shsql.models import UserProfile

# Signal for saving user profile information when a user is
# created (so we never need to call UserProfile save)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Signal for saving user profile information when a user is
# updated (so we never need to call UserProfile save)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
