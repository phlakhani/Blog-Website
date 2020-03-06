
# this file is used to create profile of user when user register first time so we dont have to create
    # from admin

## signals module is used to send signal when User create(that's why sender is user) n receiver decorator help us
  # to create and save profile from user details by function that we created

 # it's necessary to register this signal.py into apps.py of this particular app

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()
