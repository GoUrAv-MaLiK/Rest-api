"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from datetime import time, timedelta
""" SIMPLE_JWT={
    'ACCESS_TOKEN_LIFETIME':timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME':time(days=1),
    'ROTATE_REFRESH_TOKEN':False,
    'BLACK_LIST_AFTER_ROTATION':True,
    'ALGORITHM':'HS256',
    'SIGNINIG_KEY':settings.SECRET_KEY,
    
} """

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y5zcjxpym#j4vsbp3u&&%^v^dg*qupnow4x%jbp+*@$#0k&q1l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'AuthenticationPermission',
    'SessionAuhtentication',
    'AuthenticationAndPermissionsInFBV',
    'TokenAuthentication',
    'rest_framework.authtoken',
    'CustomAuthentication',
    'JSONWebToken',
    'throtling',
    'filter',
    'django_filters', #REGISTRING DJANGO FILTERS
    'pagination',
    'SerializerRelation',
    'HyperLinkModelSerializer',#in serializer.py your parent class should be serializer.HyperLinkedModelSerializer
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

ROOT_URLCONF = 'main.urls'

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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
REST_FRAMEWORK={
    # 'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework.authentication.BasicAuthentication'],
    # 'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.IsAuthenticated'],
    #to set on all the views 

    # FOR THROTTLING
    # 'DEFAULT_THROTTLE_RATES':{
    #     'anon':'2/day',#announmous user
    #     'user':'5/hour',#authenticated user
    #     'customrate':'3/minute',

    # FOR DJANGO FILTERS
    'DEFAULT_FILTER_BACKENDS':['django_filters.rest_framework.DjangoFilterBackend'],

    # FOR PAGINATION
    # 'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE':2
    }


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
