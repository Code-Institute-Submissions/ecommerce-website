from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    image = models.ImageField(upload_to="avatars", default="avatars/anonymous.png", null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    
    objects = models.Manager()
    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()