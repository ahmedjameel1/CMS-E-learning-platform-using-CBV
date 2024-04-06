import os
from .base import *
import dj_database_url


DEBUG = False

ADMINS = [
    
]

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgresql://devsearchuser:lE2yTUMIhH04gF0aMfN8y9vvN8spqa6U@dpg-co7eu3ev3ddc739568ig-a:5432/cms_db',
        conn_max_age=600
    )
}

# REDIS_URL = 'redis://cache:6379'
# CACHES['default']['LOCATION'] = REDIS_URL
# CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

# # Security
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
# and renames the files with unique names for each version to support long-term caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
