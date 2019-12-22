from .base import *
from .local import *
# importing os module  
import os 
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Python program to explain os.environ object  
  from django.utils.crypto import get_random_string


  
# Add a new environment variable  
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAT2JWHGMKF2KX3BTF'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'


chars = 'amnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = get_random_string(50, chars)