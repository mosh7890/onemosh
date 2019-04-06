from decouple import Csv
from .base import *

DEBUG = False

# environment variable in ebs config
ALLOWED_HOSTS = config('ALLOWED_HOSTS_PRODUCTION', cast=Csv())

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': config('PYTHONANYWHERE_USERNAME') + '$' + config('PYTHONANYWHERE_DB_NAME'),
            'USER': config('PYTHONANYWHERE_USERNAME'),
            'PASSWORD': config('PYTHONANYWHERE_PW'),
            'HOST': config('PYTHONANYWHERE_HOSTNAME'),
            'OPTIONS': {
                'charset': 'utf8mb4',
            },
            'TEST': {
                'NAME': config('PYTHONANYWHERE_USERNAME') + '$test_' + config('PYTHONANYWHERE_DB_NAME'),
                'CHARSET': 'utf8mb4',
                'COLLATION': 'utf8mb4_unicode_ci',
            },
        }
    }

# drf
DRF_NEW_ENTRY = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}
REST_FRAMEWORK.update(DRF_NEW_ENTRY)

# django-debug-toolbar
TOOLBAR = False
