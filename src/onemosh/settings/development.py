import logging

from decouple import Csv

from .base import *

DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS_DEV', cast=Csv())

INSTALLED_APPS += (
    'nplusone.ext.django',
)

MIDDLEWARE += [
    'nplusone.ext.django.NPlusOneMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(os.path.dirname(BASE_DIR), 'my.cnf'),
        },
        'TEST': {
            'NAME': 'test_onemosh',
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_general_ci',
        },
        'CONN_MAX_AGE': 60 * 10,
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

# temporary django email service
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# django-debug-toolbar
TOOLBAR = True

if TOOLBAR:
    INTERNAL_IPS = config('INTERNAL_IPS', cast=Csv())

    INSTALLED_APPS += (
        'debug_toolbar',
    )

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    DEBUG_TOOLBAR_CONFIG = {
        'DISABLE_PANELS': {
            'debug_toolbar.panels.redirects.RedirectsPanel'
        },
        'JQUERY_URL': '/static/js/jquery-3.3.1.min.js',
    }

# nplusone
NPLUSONE_LOGGER = logging.getLogger('nplusone')
NPLUSONE_LOG_LEVEL = logging.WARN

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'nplusone': {
            'handlers': ['console'],
            'level': 'WARN',
        },
    },
}
