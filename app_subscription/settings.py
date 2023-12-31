"""
Django settings for app_subscription project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import sys
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))
if not os.environ.get("DEBUG"):
    print("Please specify DEBUG variable in .env file")
debug = False if os.environ.get("DEBUG").lower() == "false" else True

if not os.environ.get("DATABASE_NAME"):
    print("Please specify DATABASE_NAME variable in .env file")
DATABASE_NAME = os.environ.get("DATABASE_NAME")

if not os.environ.get("DATABASE_USERNAME"):
    print("Please specify DATABASE_PASSWORD variable in .env file")
DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")

if not os.environ.get("DATABASE_PASSWORD"):
    print("Please specify DATABASE_PASSWORD variable in .env file")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

if not os.environ.get("DATABASE_HOST"):
    print("Please specify 'DATABASE_HOST' variable in .env file")
DATABASE_HOST = os.environ.get("DATABASE_HOST")

if not os.environ.get("DATABASE_PORT"):
    print("Please specify 'DATABASE_PORT' variable in .env file")
DATABASE_PORT = os.environ.get("DATABASE_PORT")

if not os.environ.get("ENGINE"):
    print("Please specify ENGINE variable in .env file")
ENGINE = os.environ.get("ENGINE")

if not os.environ.get("JWT_TOKEN_EXPIRY_DELTA"):
    print("Please specify 'JWT_TOKEN_EXPIRY_DELTA' variable in .env file")
JWT_TOKEN_EXPIRY_DELTA = os.environ.get("JWT_TOKEN_EXPIRY_DELTA")
if not os.environ.get("JWT_ENCODING_ALGO"):
    print("Please specify JWT_ENCODING_ALGO' variable in .env file")
JWT_ENCODING_ALGO = os.environ.get("JWT_ENCODING_ALGO")

if not os.environ.get("JWT_ENCODING_SECRET_KEY"):
    print("Please specify 'JWT_ENCODING_SECRET_KEY' variable in .env file")
JWT_ENCODING_SECRET_KEY = os.environ.get("JWT_ENCODING_SECRET_KEY")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i51v$708h$fte(6!h2kl5)7=0-b*&4j@qx=6%wvdb9&9=jvugq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_authentication',
    'notifications',
    'app_panel',

     # third party apps
     'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app_subscription.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'app_subscription.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# settings.py



DATABASES = {
    'default': {
        "ENGINE": ENGINE,
        "NAME": DATABASE_NAME,
        "USER": DATABASE_USERNAME,
        "PASSWORD": DATABASE_PASSWORD,
        "HOST": DATABASE_HOST,
        "PORT": DATABASE_PORT,
        'TEST': {
                    'NAME': DATABASE_USERNAME,
                },
    }
}
if 'test' in sys.argv:
    DATABASES['default']['USER'] = DATABASE_USERNAME

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/
AUTHENTICATION_BACKENDS = [
    "utils.base_authentication.AuthenticationBackend",
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',
]

EMAIL_BACKEND = ""
EMAIL_HOST = ""
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""


AUTH_USER_MODEL = "user_authentication.User"

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
