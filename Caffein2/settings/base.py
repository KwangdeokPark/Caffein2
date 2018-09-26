"""
Django settings for Caffein2 project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import json
import os

from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEBUG = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
def get_secret(setting):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        secret_file = os.path.join(BASE_DIR, 'Caffein2', 'secrets.json')
        with open(secret_file) as f:
            secrets = json.loads(f.read())
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)
    except:
        return None


SECRET_KEY = get_secret('SECRET_KEY') if get_secret('SECRET_KEY') else os.environ['SECRET_KEY']
# Application definition

INSTALLED_APPS = [
    # Bootstrap Admin
    'bootstrap_admin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # User registered apps
    'accounts',
    'cafes',
    'core',
    'meetings',
    'partners',
    'photo_albums',
    'surveys',
    'comments',
    # 3rd party apps
    'imagekit',
    'crispy_forms',
    'debug_toolbar',
    'django_user_agents',

    # AWS
    'storages',
]
USER_AGENTS_CACHE = None
SITE_ID = 1

MIDDLEWARE = [
    # DebugToolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 3rd party
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'Caffein2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Caffein2', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Custom Processors
                'core.context_processors.latest_os'
            ],
        },
    },
]

WSGI_APPLICATION = 'Caffein2.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Login settings
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Caffein2', 'static'),
]

# Media files

MEDIA_URL = '/media/'
MEDIAFILES_DIRS = [
    os.path.join(BASE_DIR, 'Caffein2', 'media'),
]

# User Model
AUTH_USER_MODEL = 'accounts.User'


# Messages(alert.error -> alert.danger)
from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {message_constants.DEBUG: 'debug',
                message_constants.INFO: 'info',
                message_constants.SUCCESS: 'success',
                message_constants.WARNING: 'warning',
                message_constants.ERROR: 'danger', }
# Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# NaverMap
if DEBUG:
    NAVER_CLIENT_ID = get_secret("NAVER_CLIENT_ID")
    NAVER_CLIENT_SECRET = get_secret("NAVER_CLIENT_SECRET")
else:
    NAVER_CLIENT_ID = os.environ['NAVER_CLIENT_ID']
    NAVER_CLIENT_SECRET = os.environ['NAVER_CLIENT_SECRET']
