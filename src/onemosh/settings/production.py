from decouple import Csv
from .base import *

DEBUG = False

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

# temporary django email service
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# django-debug-toolbar
TOOLBAR = False
