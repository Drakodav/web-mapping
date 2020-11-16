"""
Django settings for django_tutorial project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k)(-p1!ad(=&_fh_5+()x1fofdabp-6^dp#e74@z)(v!0$*wv+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'pwa',
    'leaflet',
    'world',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # serve static files
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_tutorial.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'accounts/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOGIN_REDIRECT_URL = 'home'
WSGI_APPLICATION = 'django_tutorial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gis',
        'USER': 'docker',
        'PASSWORD': 'docker',
        'HOST': 'localhost',
        'PORT': '25432',
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# leaflet config
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (53.0, -8.0),
    'DEFAULT_ZOOM': 6,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
    'RESET_VIEW': False,
    'SCALE': None,
    'OPACITY': 0.5,
    'FORCE_IMAGE_PATH': True
}

# email configs
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/static")
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/dist/'),
    os.path.join(BASE_DIR, 'frontend/dist/static'),
    os.path.join(BASE_DIR, 'staticfiles/bootstrap'),
    os.path.join(BASE_DIR, 'staticfiles/icons'),
]

if socket.gethostname() == "DESKTOP-9D122S4":
    DATABASES["default"]["HOST"] = "localhost"
    DATABASES["default"]["PORT"] = 25432

    DEBUG = True
    TEMPLATES[0]["OPTIONS"]["debug"] = True
    ALLOWED_HOSTS = ['*', ]
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False
else:
    DATABASES["default"]["HOST"] = 'postgis'
    DATABASES["default"]["PORT"] = 5432

    ALLOWED_HOSTS = ['.thev-lad.com', 'localhost']
    # DEBUG = False
    # TEMPLATES[0]["OPTIONS"]["debug"] = False
    # CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    # PWA_APP_DEBUG_MODE = False


# PWA configuration manifest
PWA_SERVICE_WORKER_PATH = os.path.join(
    BASE_DIR, 'frontend/dist/service-worker.js')
PWA_APP_DEBUG_MODE = True

PWA_APP_NAME = 'geoLad'
PWA_APP_DESCRIPTION = "AWM"
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/icons/splash.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
PWA_APP_ICONS = [
    {
        "src": "/static/images/icons/icon-72x72.png",
        "sizes": "72x72",
        "type": "image/png"
    },
    {
        "src": "/static/images/icons/icon-96x96.png",
        "sizes": "96x96",
        "type": "image/png"
    },
    {
        "src": "/static/images/icons/icon-128x128.png",
        "sizes": "128x128",
        "type": "image/png"
    },
    {
        "src": "/static/images/icons/icon-144x144.png",
        "sizes": "144x144",
        "type": "image/png"
    },
    {
        "src": "/static/images/icons/icon-152x152.png",
        "sizes": "152x152",
        "type": "image/png"
    },
    {
        "src": "/static/images/icons/icon-192x192.png",
        "sizes": "192x192",
        "type": "image/png"
    },
    {
        "src": "/static/images/icons/icon-384x384.png",
        "sizes": "384x384",
        "type": "image/png"
    },
    {
        "src": "/static/images/icons/icon-512x512.png",
        "sizes": "512x512",
        "type": "image/png"
    }
]
PWA_APP_ICONS_APPLE = PWA_APP_ICONS
