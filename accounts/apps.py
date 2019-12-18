from django.apps import AppConfig
 from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from cmdbox.profiles.signals import create_user_profile, save_user_profile

class AccountsConfig(AppConfig):
    name = 'accounts'
    verbose_name = _('accounts-profiles')


    def ready(self):
        post_save.connect(create_user_profile, sender=User)
        post_save.connect(save_user_profile, sender=User)       