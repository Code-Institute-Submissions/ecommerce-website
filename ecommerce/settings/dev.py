from .base import *
from .local import *
# importing os module  
import os 
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Python program to explain os.environ object  
from django.utils.crypto import get_random_string

ARN_bucket = 'arn:aws:s3:::mybucket-last'
  
# Add a new environment variable  
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAT2JWHGMKESRDYD25'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'


chars = 'amnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = get_random_string(50, chars)