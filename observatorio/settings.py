"""
Django settings for observatorio project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from cassandra import ConsistencyLevel

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r6ffrkof2^qr@9d2(+^!7xxbmzg$vh@11!cq-z_bn2s^9^sp(r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
  'django_cassandra_engine',
  'l4_app',
  'reportes',
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'l4_app.middleware.RequireLoginMiddleware',
]

ROOT_URLCONF = 'observatorio.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'observatorio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'OPTIONS': {
      'read_default_file': os.path.join(BASE_DIR, 'mysql_obs.cnf'),
    }
  },
  'cass_db': {
    'ENGINE': 'django_cassandra_engine',
    'NAME': 'btpucp',
    'TEST_NAME': 'test_db',
    'HOST': '127.0.0.1',
    'PORT': 9042,
    'OPTIONS': {
      'replication': {
        'strategy_class': 'SimpleStrategy',
        'replication_factor': 1
      },
      'connection': {
          'consistency': ConsistencyLevel.ALL,
          'retry_connect': True
          # + All connection options for cassandra.cluster.Cluster()
      },
      'session': {
          'default_timeout': 10,
          'default_fetch_size': 10000
          # + All options for cassandra.cluster.Session()
      }
    }
  }
}

DATABASE_ROUTERS = ['l4_app.routers.CustomRouter']

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'