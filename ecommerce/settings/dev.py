from .base import *
# importing os module  
import os 
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Python program to explain os.environ object  
  

  
# Add a new environment variable  
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAT2JWHGMKNZ53HD6P'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
