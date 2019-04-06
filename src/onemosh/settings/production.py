from decouple import Csv
from .base import *

DEBUG = False

# environment variable in ebs config
ALLOWED_HOSTS = config('ALLOWED_HOSTS_PRODUCTION', cast=Csv())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('PYTHONANYWHERE_USERNAME') + '$' + config('PYTHONANYWHERE_DB_NAME'),
        'USER': config('PYTHONANYWHERE_USERNAME'),
        'PASSWORD': config('PYTHONANYWHERE_PW'),
        'HOST': config('PYTHONANYWHERE_HOSTNAME'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        'TEST': {
            'NAME': config('PYTHONANYWHERE_USERNAME') + '$test_' + config('PYTHONANYWHERE_DB_NAME'),
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_general_ci',
        },
    }
}

# static files (css, javaScript, images)
# python manage.py collectstatic will use these paths to store static files
# noinspection PyUnresolvedReferences
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), '.', 'www', 'static')
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), '.', 'www', 'media')

# urls to use when serving static files located in STATIC_ROOT/MEDIA_ROOT.
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# project folders to search when using {% load static %}; currently checks src/static/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# drf
DRF_NEW_ENTRY = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}
REST_FRAMEWORK.update(DRF_NEW_ENTRY)

# django-debug-toolbar
TOOLBAR = False
